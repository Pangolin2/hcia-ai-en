import os
import re
import tarfile
import urllib.request
from collections import Counter

import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.model_selection import train_test_split
from torch.utils.data import DataLoader, Dataset


# Set a random seed.
torch.manual_seed(42)


def download_imdb(data_dir):
    # Create a data directory.
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    # Download the IMDb dataset.
    url = "https://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz"
    file_path = os.path.join(data_dir, "aclImdb_v1.tar.gz")

    if not os.path.exists(file_path):
        print("Downloading IMDB dataset...")
        urllib.request.urlretrieve(url, file_path)
        print("Download complete.")

    # Decompress the file.
    if not os.path.exists(os.path.join(data_dir, "aclImdb")):
        print("Extracting IMDB dataset...")
        with tarfile.open(file_path, "r:gz") as tar:
            tar.extractall(path=data_dir)
        print("Extraction complete.")


def load_imdb_data(data_dir):
    reviews = []
    labels = []

    for label_type in ['pos', 'neg']:
        dir_name = os.path.join(data_dir, 'aclImdb', 'train', label_type)
        for fname in os.listdir(dir_name):
            if fname.endswith('.txt'):
                with open(os.path.join(dir_name, fname), 'r', encoding='utf-8') as f:
                    reviews.append(f.read())
                labels.append(1 if label_type == 'pos' else 0)

    return reviews, labels


# Preprocess text.
def preprocess_text(text):
    text = re.sub(r'[^\w\s]', '', text) # Removal of punctuations
    text = text.lower() # Conversion to lowercase
    return text


# Build a vocabulary.
def build_vocab(reviews, max_vocab_size=10000):
    word_counts = Counter()
    for review in reviews:
        word_counts.update(review.split())
    vocab = {word: i + 1 for i, (word, _) in enumerate(word_counts.most_common(max_vocab_size))}
    vocab['<PAD>'] = 0 # Addition of padding characters
    return vocab


# Convert the text into index sequences.
def text_to_sequence(text, vocab):
    return [vocab.get(word, 0) for word in text.split()]


# Pad the sequences.
def pad_sequence(seq, max_len):
    if len(seq) >= max_len:
        return seq[:max_len]
    return seq + [0] * (max_len - len(seq))


class IMDBDataset(Dataset):
    def __init__(self, X, y):
        self.X = X
        self.y = y

    def __len__(self):
        return len(self.X)

    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]


class TextCNN(nn.Module):
    def __init__(self, vocab_size, embed_dim, num_classes, kernel_sizes=[3, 4, 5], num_filters=100):
        super(TextCNN, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim)
        self.convs = nn.ModuleList([
            nn.Conv2d(1, num_filters, (k, embed_dim)) for k in kernel_sizes
        ])
        self.fc = nn.Linear(len(kernel_sizes) * num_filters, num_classes)
        self.dropout = nn.Dropout(0.5)

    def forward(self, x):
        x = self.embedding(x)
        x = x.unsqueeze(1)
        x = [torch.relu(conv(x)).squeeze(3) for conv in self.convs]
        x = [torch.max_pool1d(i, i.size(2)).squeeze(2) for i in x]
        x = torch.cat(x, 1)
        x = self.dropout(x)
        x = self.fc(x)
        return x


def train_model(model, train_loader, criterion, optimizer, device, num_epochs=10):
    model.to(device)
    model.train()

    for epoch in range(num_epochs):
        total_loss = 0
        for batch_X, batch_y in train_loader:
            batch_X, batch_y = batch_X.to(device), batch_y.to(device)
            optimizer.zero_grad()
            outputs = model(batch_X)
            loss = criterion(outputs, batch_y)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()

        print(f'Train-Epoch [{epoch + 1}/{num_epochs}], Loss: {total_loss / len(train_loader):.4f}')


def test_model(model, test_loader, device):
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for batch_X, batch_y in test_loader:
            batch_X, batch_y = batch_X.to(device), batch_y.to(device)
            outputs = model(batch_X)
            _, predicted = torch.max(outputs.data, 1)
            total += batch_y.size(0)
            correct += (predicted == batch_y).sum().item()

    print(f'Test Accuracy: {100 * correct / total:.2f}%')


def predict_sentiment(text, model, vocab, device, max_len=200):
    text = preprocess_text(text)
    sequence = text_to_sequence(text, vocab)
    sequence = pad_sequence(sequence, max_len)
    sequence = torch.tensor(sequence, dtype=torch.long).unsqueeze(0).to(device)
    with torch.no_grad():
        output = model(sequence)
        _, predicted = torch.max(output, 1)
    return "pos" if predicted.item() == 1 else "neg"


if __name__ == "__main__":
    # Download and load data.
    data_dir = "data/imdb"
    download_imdb(data_dir)
    reviews, labels = load_imdb_data(data_dir)

    # Preprocess data.
    reviews = [preprocess_text(review) for review in reviews]
    vocab = build_vocab(reviews)
    sequences = [text_to_sequence(review, vocab) for review in reviews]

    # Pad the sequences and split the dataset.
    max_len = 200
    X = [pad_sequence(seq, max_len) for seq in sequences]
    X = torch.tensor(X, dtype=torch.long)
    y = torch.tensor(labels, dtype=torch.long)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create datasets and data loaders.
    train_dataset = IMDBDataset(X_train, y_train)
    test_dataset = IMDBDataset(X_test, y_test)
    train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=64, shuffle=False)

    # Define the model, loss function, and optimizer.
    vocab_size = len(vocab)
    embed_dim = 100
    num_classes = 2
    model = TextCNN(vocab_size, embed_dim, num_classes)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    # Obtain the device.
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f'Using device: {device}')

    # Train the model.
    train_model(model, train_loader, criterion, optimizer, device, num_epochs=10)

    # Test the model.
    test_model(model, test_loader, device)

    # Save the model.
    model_path = "textcnn_model.pth"
    torch.save(model.state_dict(), model_path)
    print(f"Model saved to {model_path}")

    # Test two English texts.
    test_texts = [
        "This movie is absolutely fantastic! The acting was superb and the plot was engaging.",
        "I hated this movie. It was boring and the characters were poorly developed.",
    ]
    for text in test_texts:
        sentiment = predict_sentiment(text, model, vocab, device)
        print(f"Text: {text}\nsentiment: {sentiment}\n")
