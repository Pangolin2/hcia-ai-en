import os
import random

import matplotlib.pyplot as plt
import numpy as np
import torch
import torchvision
from PIL import Image
from torch.utils.data import DataLoader, Dataset
from torchvision import datasets, transforms


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


# 1.2.1 Creating a Tensor
x = torch.rand(4, 3)
print(x)

print(torch.Tensor(np.array([[1, 2], [3, 4]]))) # Use an array to create a tensor.
print(torch.Tensor([True, False])) # Use bool data to create a tensor.
print(torch.Tensor((1, 2, 3, 4, 5))) # Use a tuple to create a tensor.
print(torch.Tensor([i for i in range(10)])) # Use a list to create a tensor.

print(torch.FloatTensor(2, 3).type()) # Build a 2 x 3 tensor of the float type.
print(torch.DoubleTensor(2, 3).type()) # Build a 2 x 3 tensor of the double type.
print(torch.HalfTensor(2, 3).type()) # Build a 2 x 3 tensor of the HalfTensor type.
print(torch.ByteTensor(2, 3).type()) # Build a 2 x 3 tensor of the byte type.
print(torch.CharTensor(2, 3).type()) # Build a 2 x 3 tensor of the char type.
print(torch.ShortTensor(2, 3).type()) # Build a 2 x 3 tensor of the short type.
print(torch.IntTensor(2, 3).type()) # Build a 2 x 3 tensor of the Int type.
print(torch.LongTensor(2, 3).type()) # Build a 2 x 3 tensor of the long type.

x = torch.zeros(4, 3, dtype=torch.long)
print(x) # All-zero tensor
x = torch.ones(4, 3, dtype=torch.long)
print(x) # All-1 tensor
x = x.new_ones(4, 3, dtype=torch.double)
print(x)
x = torch.randn_like(x, dtype=torch.float)
print(x)


# 1.2.2 Tensor Attributes
x = torch.Tensor(np.array([[1, 2], [3, 4]]))
print(x.shape) # Obtain the shape.
print(x.size())
print(x.dim()) # Number of dimensions
print(x.device) # Hardware
print(x.dtype) # Data type


# 1.2.3 Tensor Method
x = torch.Tensor(np.array([[1, 2], [3, 4]]))

print(x.reshape(4, 1)) # reshape
x = x.unsqueeze(2) # Add a dimension.
print(x.shape)
x = x.squeeze(2) # Compress dimensions.
print(x.shape)

print(x.flatten()) # Flatten to one dimension.
x.to(device) # Move to the specified device.


# 1.2.4 Loading the Dataset
train_dataset = datasets.MNIST(
    root='./MNIST',
    train=True,
    download=True,
    transform=transforms.ToTensor(),
)

plt.figure(figsize=(8, 8))
i = 1

for dic in train_dataset.data[:3]:
    plt.subplot(3, 3, i)
    plt.imshow(dic)
    plt.axis('off')
    i += 1
plt.show()


# Use ImageFolder to load the dataset.
if os.path.exists("./flower_photos_train/"):
    train = torchvision.datasets.ImageFolder("./flower_photos_train/", transform=transforms.ToTensor())

    print("Dataset types")
    print(train.classes)
    print(train.class_to_idx)
    print("Dataset samples")
    print(train.samples[0])
    print("Image data format")
    print(train.extensions[0])

    # Display the loaded image data.
    for i in range(5):
        plt.figure()
        random.seed(2)
        num = random.randint(0, min(3000, len(train) - 1))
        plt.imshow(train[num][0].permute(1, 2, 0))
        plt.title(train[num][1])
        plt.colorbar()
        plt.grid(False)
    plt.show()


class CustomDataset(Dataset):
    def __init__(self, image_dir, label_file, transform=None):
        self.image_dir = image_dir # Image directory
        self.labels = self._load_labels(label_file) # Load labels.
        self.image_filenames = sorted(os.listdir(image_dir)) # Obtain the image file name list and sort the files.
        self.transform = transform # Image transformation

    def _load_labels(self, label_file):
        with open(label_file, 'r') as f:
            labels = [int(line.strip()) for line in f]
        return labels

    def __len__(self):
        return len(self.image_filenames)

    def __getitem__(self, idx):
        img_name = os.path.join(self.image_dir, self.image_filenames[idx])
        image = Image.open(img_name).convert('RGB')
        label = self.labels[idx]

        if self.transform:
            image = self.transform(image)

        return image, label


if __name__ == "__main__":
    transform = transforms.Compose([
        transforms.ToTensor(),
    ])

    image_dir = 'path/to/images'
    label_file = 'path/to/labels.txt'

    if os.path.exists(image_dir) and os.path.exists(label_file):
        dataset = CustomDataset(image_dir=image_dir, label_file=label_file, transform=transform)
        dataloader = DataLoader(dataset, batch_size=32, shuffle=True, num_workers=4)
        print(dataloader)
