import base64
import os
import random

import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
from easydict import EasyDict as edict


# Download the data file.
# !pip install download
#
# from download import download
# url_train = (
#     b"aHR0cHM6Ly9hc2NlbmQtcHJvZmVzc2lvbmFsLWNvbnN0cnVjdGlvbi1kYXRhc2V0Lm9icy5teWh1YXdlaW"
#     b"Nsb3VkLmNvbS9kZWVwLWxlYXJuaW5nL2Zsb3dlcl9waG90b3NfdHJhaW4uemlw"
# )
# url_test = (
#     b"aHR0cHM6Ly9hc2NlbmQtcHJvZmVzc2lvbmFsLWNvbnN0cnVjdGlvbi1kYXRhc2V0Lm9icy5teWh1YXdlaW"
#     b"Nsb3VkLmNvbS9kZWVwLWxlYXJuaW5nL2Zsb3dlcl9waG90b3NfdGVzdC56aXA="
# )
# path_train = download(base64.b64decode(url_train).decode(), "./", kind="zip", replace=True, verbose=False)
# path_test = download(base64.b64decode(url_test).decode(), "./", kind="zip", replace=True, verbose=False)


cfg = edict({
    'data_path': './flower_photos_train', # Path of the training dataset
    'test_path': './flower_photos_test', # Path of the test dataset
    'data_size': 3616,
    'HEIGHT': 224, # Image height
    'WIDTH': 224, # Image width
    '_R_MEAN': 123.68, # Mean of CIFAR10
    '_G_MEAN': 116.78,
    '_B_MEAN': 103.94,
    '_R_STD': 1, # User-defined standard deviation
    '_G_STD': 1,
    '_B_STD': 1,
    '_RESIZE_SIDE_MIN': 256, # Minimum resize value of image enhancement
    '_RESIZE_SIDE_MAX': 512,

    'batch_size': 1, # Batch size
    'num_class': 5, # Classification
    'epoch_size': 5, # Number of training times
    'num_workers': 1,
    'device': "cpu", # cpu, xpu, etc.

    'prefix': 'renet50.pth', # Model name
})


# Use transforms.Compose to combine multiple processing modes.
transform_train = transforms.Compose([
    transforms.RandomHorizontalFlip(),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[cfg._R_MEAN, cfg._G_MEAN, cfg._B_MEAN],
        std=[cfg._R_STD, cfg._G_STD, cfg._B_STD],
    ),
    transforms.Resize(cfg._RESIZE_SIDE_MIN),
    transforms.CenterCrop((cfg.HEIGHT, cfg.WIDTH)),
])

transform_test = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
])


train = torchvision.datasets.ImageFolder(cfg.data_path, transform=transform_train)
trainloader = torch.utils.data.DataLoader(
    train,
    batch_size=cfg.batch_size,
    shuffle=True,
    num_workers=cfg.num_workers,
)


# Define the basic block, which is mainly used for ResNet-18 and ResNet-34.
class BasicBlock(nn.Module):
    expansion = 1 # Multiple for expansion of the number of output channels

    def __init__(self, in_channels, out_channels, stride=1):
        super(BasicBlock, self).__init__()

        # Residual function
        self.residual_function = nn.Sequential(
            nn.Conv2d(in_channels, out_channels, kernel_size=3, stride=stride, padding=1, bias=False),
            nn.BatchNorm2d(out_channels),
            nn.ReLU(inplace=True),
            nn.Conv2d(out_channels, out_channels * BasicBlock.expansion, kernel_size=3, padding=1, bias=False),
            nn.BatchNorm2d(out_channels * BasicBlock.expansion),
        )

        # Shortcut, which is used to adjust the dimensions and stride
        self.shortcut = nn.Sequential()

        # If the dimensions do not match, use 1x1 convolution to adjust the dimensions of the shortcut.
        if stride != 1 or in_channels != BasicBlock.expansion * out_channels:
            self.shortcut = nn.Sequential(
                nn.Conv2d(
                    in_channels,
                    out_channels * BasicBlock.expansion,
                    kernel_size=1,
                    stride=stride,
                    bias=False,
                ),
                nn.BatchNorm2d(out_channels * BasicBlock.expansion),
            )

    def forward(self, x):
        # Residual connection and activation function
        return nn.ReLU(inplace=True)(self.residual_function(x) + self.shortcut(x))


# Define the bottleneck block, which is mainly used for ResNet-50, ResNet-101, and ResNet-152.
class BottleNeck(nn.Module):
    expansion = 4 # Multiple for expansion of the number of output channels

    def __init__(self, in_channels, out_channels, stride=1):
        super(BottleNeck, self).__init__()

        # Residual function
        self.residual_function = nn.Sequential(
            nn.Conv2d(in_channels, out_channels, kernel_size=1, bias=False),
            nn.BatchNorm2d(out_channels),
            nn.ReLU(inplace=True),
            nn.Conv2d(out_channels, out_channels, stride=stride, kernel_size=3, padding=1, bias=False),
            nn.BatchNorm2d(out_channels),
            nn.ReLU(inplace=True),
            nn.Conv2d(out_channels, out_channels * BottleNeck.expansion, kernel_size=1, bias=False),
            nn.BatchNorm2d(out_channels * BottleNeck.expansion),
        )

        # Shortcut, which is used to adjust the dimensions and stride
        self.shortcut = nn.Sequential()

        # If the dimensions do not match, use 1x1 convolution to adjust the dimensions of the shortcut.
        if stride != 1 or in_channels != out_channels * BottleNeck.expansion:
            self.shortcut = nn.Sequential(
                nn.Conv2d(
                    in_channels,
                    out_channels * BottleNeck.expansion,
                    stride=stride,
                    kernel_size=1,
                    bias=False,
                ),
                nn.BatchNorm2d(out_channels * BottleNeck.expansion),
            )

    def forward(self, x):
        # Residual connection and activation function
        return nn.ReLU(inplace=True)(self.residual_function(x) + self.shortcut(x))


# Define the ResNet network.
class ResNet(nn.Module):
    def __init__(self, block, num_block, num_classes=100):
        super(ResNet, self).__init__()

        self.in_channels = 64 # Initial number of channels

        # The first convolutional layer
        self.conv1 = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=3, padding=1, bias=False),
            nn.BatchNorm2d(64),
            nn.ReLU(inplace=True),
        )

        # The number of layers varies depending on the ResNet version.
        self.conv2_x = self._make_layer(block, 64, num_block[0], 1)
        self.conv3_x = self._make_layer(block, 128, num_block[1], 2)
        self.conv4_x = self._make_layer(block, 256, num_block[2], 2)
        self.conv5_x = self._make_layer(block, 512, num_block[3], 2)

        # Global average pooling layer
        self.avg_pool = nn.AdaptiveAvgPool2d((1, 1))

        # Fully-connected layer. Set the number of output classes as required.
        self.fc = nn.Linear(512 * block.expansion, num_classes)

    def _make_layer(self, block, out_channels, num_blocks, stride):
        # Generate a sequence of layers.
        strides = [stride] + [1] * (num_blocks - 1)
        layers = []
        for stride in strides:
            layers.append(block(self.in_channels, out_channels, stride))
            self.in_channels = out_channels * block.expansion

        return nn.Sequential(*layers)

    def forward(self, x):
        # Forward propagation
        output = self.conv1(x)
        output = self.conv2_x(output)
        output = self.conv3_x(output)
        output = self.conv4_x(output)
        output = self.conv5_x(output)
        output = self.avg_pool(output)
        output = output.view(output.size(0), -1)
        output = self.fc(output)

        return output


# Define ResNets of different versions.
def resnet18():
    """Return the ResNet-18 model"""
    return ResNet(BasicBlock, [2, 2, 2, 2])


def resnet34():
    """Return the ResNet-34 model"""
    return ResNet(BasicBlock, [3, 4, 6, 3])


def resnet50():
    """Return the ResNet-50 model"""
    return ResNet(BottleNeck, [3, 4, 6, 3], num_classes=cfg.num_class)


def resnet101():
    """Return the ResNet-101 model"""
    return ResNet(BottleNeck, [3, 4, 23, 3])


def resnet152():
    """Return the ResNet-152 model"""
    return ResNet(BottleNeck, [3, 8, 36, 3])


net = resnet50().to(cfg.device)
if os.path.isfile(cfg.prefix):
    net.load_state_dict(torch.load(cfg.prefix))


criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(), lr=0.1, momentum=0.9, weight_decay=0.0001)
scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer, factor=0.1, patience=5)


for epoch in range(cfg.epoch_size):
    losses = []
    running_loss = 0
    for i, inp in enumerate(trainloader):
        inputs, labels = inp
        inputs, labels = inputs.to(cfg.device), labels.to(cfg.device)
        optimizer.zero_grad()

        outputs = net(inputs)
        loss = criterion(outputs, labels)
        losses.append(loss.item())

        loss.backward()
        optimizer.step()

        running_loss += loss.item()

        if i % 200 == 0 and i > 0:
            print(f'Loss [{epoch + 1}, {i}](epoch, minibatch): ', running_loss / 100)
            running_loss = 0.0

    avg_loss = sum(losses) / len(losses)
    scheduler.step(avg_loss)

print('Training Done')


torch.save(net.state_dict(), cfg.prefix)


test = torchvision.datasets.ImageFolder(cfg.test_path, transform=transform_test)
testloader = torch.utils.data.DataLoader(
    test,
    batch_size=cfg.batch_size,
    shuffle=True,
    num_workers=cfg.num_workers,
)

correct = 0
total = 0

with torch.no_grad():
    for data in testloader:
        images, labels = data
        images, labels = images.to(cfg.device), labels.to(cfg.device)
        outputs = net(images)

        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()
print('Accuracy: ', 100 * (correct / total), '%')
