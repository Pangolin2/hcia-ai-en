# coding: utf-8
import gzip
import os
import pickle

import numpy as np


key_file = {
    'train_img': 'train-images-idx3-ubyte.gz',
    'train_label': 'train-labels-idx1-ubyte.gz',
    'test_img': 't10k-images-idx3-ubyte.gz',
    'test_label': 't10k-labels-idx1-ubyte.gz',
}

dataset_dir = os.path.dirname(os.path.abspath(__file__))
save_file = dataset_dir + "/mnist.pkl"


def _resolve_dataset_path(file_name):
    gz_path = os.path.join(dataset_dir, file_name)
    if os.path.exists(gz_path):
        return gz_path

    raw_name = file_name[:-3] if file_name.endswith(".gz") else file_name
    raw_path = os.path.join(dataset_dir, raw_name)
    if os.path.exists(raw_path):
        return raw_path

    raise FileNotFoundError(
        "MNIST dataset file not found: {} or {}".format(gz_path, raw_path)
    )


def _open_dataset_file(file_path):
    if file_path.endswith(".gz"):
        return gzip.open(file_path, 'rb')
    return open(file_path, 'rb')


def _load_label(file_name):
    file_path = _resolve_dataset_path(file_name)

    print("Converting " + os.path.basename(file_path) + " to NumPy Array ...")
    with _open_dataset_file(file_path) as f:
        labels = np.frombuffer(f.read(), np.uint8, offset=8)
    print("Done")

    return labels


def _load_img(file_name):
    file_path = _resolve_dataset_path(file_name)

    print("Converting " + os.path.basename(file_path) + " to NumPy Array ...")
    with _open_dataset_file(file_path) as f:
        data = np.frombuffer(f.read(), np.uint8, offset=16)
    data = data.reshape(-1, 784)
    print("Done")

    return data


def _convert_numpy():
    dataset = {}
    dataset['train_img'] = _load_img(key_file['train_img'])
    dataset['train_label'] = _load_label(key_file['train_label'])
    dataset['test_img'] = _load_img(key_file['test_img'])
    dataset['test_label'] = _load_label(key_file['test_label'])

    return dataset


def init_mnist():
    dataset = _convert_numpy()
    print("Creating pickle file ...")
    with open(save_file, 'wb') as f:
        pickle.dump(dataset, f, -1)
    print("Done!")


def _change_one_hot_label(X):
    T = np.zeros((X.size, 10))
    for idx, row in enumerate(T):
        row[X[idx]] = 1
    return T


def load_mnist(normalize=True, flatten=True, one_hot_label=False):
    """Read the MNIST dataset."""
    if not os.path.exists(save_file):
        init_mnist()

    with open(save_file, 'rb') as f:
        dataset = pickle.load(f)

    if normalize:
        for key in ('train_img', 'test_img'):
            dataset[key] = dataset[key].astype(np.float32)
            dataset[key] /= 255.0

    if one_hot_label:
        dataset['train_label'] = _change_one_hot_label(dataset['train_label'])
        dataset['test_label'] = _change_one_hot_label(dataset['test_label'])

    if not flatten:
        for key in ('train_img', 'test_img'):
            dataset[key] = dataset[key].reshape(-1, 1, 28, 28)

    return (dataset['train_img'], dataset['train_label']), (dataset['test_img'], dataset['test_label'])
