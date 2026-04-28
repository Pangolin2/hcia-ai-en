# 02 Deep Learning Experiment: Fully Connected Neural Network from Scratch

## 1. Experiment Scope

This directory corresponds to the lab guide experiment:

```text
Building a Fully-Connected Neural Network from Scratch
```

The goal is to build a multi-layer fully connected neural network with Python and NumPy, then use the MNIST dataset for handwritten digit recognition. The experiment avoids high-level deep learning frameworks and exposes the core components behind neural network fitting and evaluation.

## 2. Capability Focus

| Area | Description |
|---|---|
| Data loading | Read MNIST image and label files |
| Model construction | Build a multi-layer fully connected network with 784 input features and 10 output classes |
| Loss calculation | Compute the loss during fitting |
| Gradient calculation | Use backpropagation to calculate parameter gradients |
| Parameter update | Compare SGD, Momentum, AdaGrad, and Adam |
| Result visualization | Plot loss curves for different optimizers |

## 3. Project Structure

```text
MNIST/
├── functions.py
├── gradient.py
├── layers.py
├── load_mnist.py
├── multi_layer_net.py
├── optimizer.py
├── train_mnist.py
└── util.py
```

## 4. File Roles

| File | Role |
|---|---|
| `train_mnist.py` | Main entry point |
| `load_mnist.py` | MNIST loading utilities |
| `multi_layer_net.py` | Multi-layer network implementation |
| `layers.py` | Basic layers such as affine, activation, and softmax-with-loss |
| `gradient.py` | Numerical gradient helper |
| `optimizer.py` | Optimizer implementations |
| `util.py` | Utility functions such as loss smoothing |
| `functions.py` | Activation and loss helper functions |

## 5. Data Files

The original guide expects MNIST files in the same directory. Add these files later if needed:

```text
t10k-images-idx3-ubyte
t10k-labels-idx1-ubyte
train-images-idx3-ubyte
train-labels-idx1-ubyte
```

`load_mnist.py` supports both `.gz` and non-`.gz` filenames.

## 6. Run

```bash
cd lab_manual/02_deep_learning_fully_connected_nn_from_scratch/MNIST
python3 train_mnist.py
```
