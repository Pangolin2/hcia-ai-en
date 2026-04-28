# HCIA-AI V4.0 Lab Guide: Overall Experiment Framework

## 1. Summary

The HCIA-AI V4.0 lab guide is organized as a progressive AI skills path rather than a single-tool walkthrough:

```text
Classical machine learning algorithms
  -> neural network internals
  -> PyTorch-based model development
  -> CV/NLP task practice
  -> local LLM deployment and API calling
```

The overall goal is to help learners move from algorithm usage to model-building workflows, framework-based implementation, and basic LLM service integration.

## 2. Source Scope

| Source | Role |
|---|---|
| `source_pdf/hcia-ai-v4.0-lab-guide.pdf` | Main source for experiments and procedures |
| `source_pdf/hcia-ai-v4.0-training-material.pdf` | Theory background for machine learning, deep learning, foundation models, PyTorch, and AI workflows |
| `source_pdf/hcia-ai-v4.0-exam-outline.pdf` | Exam domains and topic weights |
| `source_pdf/hcia-ai-v4.0-version-instruction.pdf` | V4.0 changes, including PyTorch, fully connected network, and LLaMA.cpp experiments |

## 3. Experiment Modules

| Module | Topics | Tools | Capability Focus | Related Exam Area |
|---|---|---|---|---|
| Machine Learning Experiments | Linear Regression, Gradient Descent, Logistic Regression, Decision Tree, K-means | `scikit-learn`, `numpy`, `matplotlib` | Understand data, model fitting, prediction, and visualization | Machine Learning Overview |
| Deep Learning Experiment | Fully connected neural network from scratch | Python, NumPy, MNIST | Understand forward pass, loss, backpropagation, gradients, and optimizers | Basics of Deep Learning and Foundation Models |
| AI Development Framework Experiment | Tensor, Dataset, LeNet, ResNet-50, TextCNN | PyTorch, torchvision | Build models and data pipelines with a mainstream framework | AI Development Framework |
| Model Deployment and Application Experiment | CLI LLM deployment, web service deployment, API calling | `llama.cpp`, DeepSeek-R1-Distill-Qwen-1.5B, HTTP APIs | Run a local model service and call it from Python | AI Business Process Overview, Foundation Models |

## 4. Capability Progression

### 4.1 Classical Machine Learning

The Machine Learning Lab Guide contains five experiments:

| Experiment | Topic | Focus |
|---|---|---|
| 1 | Linear Regression | Use `scikit-learn` to fit a simple regression model |
| 2 | Linear Regression Expansion | Implement linear regression and gradient descent with `numpy` |
| 3 | Logistic Regression | Use logistic regression for binary classification |
| 4 | Decision Tree | Build and visualize a rule-based classifier |
| 5 | K-means | Generate data and perform unsupervised clustering |

This section is short, visual, and algorithm-oriented. It is best used to verify core concepts such as features, labels, fitting, prediction, classification, regression, and clustering.

### 4.2 Neural Network Internals

The fully connected neural network experiment uses Python and NumPy to work with MNIST. It demonstrates the core components behind deep learning frameworks:

| Component | Role |
|---|---|
| Data loading | Read MNIST images and labels |
| Model structure | Build a multi-layer fully connected network |
| Loss calculation | Measure prediction error |
| Gradient calculation | Support backpropagation |
| Optimizer comparison | Compare SGD, Momentum, AdaGrad, and Adam |
| Result visualization | Plot loss curves |

This module is the bridge between theory and framework usage.

### 4.3 PyTorch-Based Development

The PyTorch section moves from basic syntax to complete tasks:

| Submodule | Content | Focus |
|---|---|---|
| PyTorch Basics | Tensor creation, tensor attributes, tensor methods | Understand core data structures |
| Dataset Loading | MNIST, ImageFolder, custom Dataset | Understand data pipelines |
| LeNet | CIFAR-10 image classification | Build a small CNN |
| ResNet-50 | Flower image classification | Build a deeper residual network |
| TextCNN | IMDb text classification | Apply CNN-style modeling to text |

This section turns the previous low-level understanding into framework-based implementation patterns.

### 4.4 LLM Deployment and API Calling

The model deployment module contains two experiments:

| Experiment | Content | Focus |
|---|---|---|
| CLI-based LLM Deployment | Run a quantized DeepSeek model with `llama.cpp` | Local command-line inference |
| Web-based LLM Deployment | Start a web service and call HTTP/OpenAI-compatible APIs | Service status checks, Python requests, OpenAI-style client calls |

This module introduces a practical deployment entry point. It does not train a large model; it focuses on running, serving, and calling a local model.

## 5. V4.0 Design Direction

The V4.0 lab guide shifts from product-platform operations toward general-purpose model development and LLM application workflows.

| Area | V4.0 Direction |
|---|---|
| Machine Learning | Keeps classical algorithm foundations |
| Deep Learning | Adds a full neural network implementation from scratch |
| AI Development Framework | Emphasizes PyTorch basics, network construction, and image classification |
| Model Deployment | Adds LLaMA.cpp-based local model deployment and API calling |
| ModelArts | Removed from the lab guide scope |

## 6. Recommended Organization

| Stage | Theme | Purpose |
|---|---|---|
| 1 | Machine learning algorithms | Build the basic data-model-prediction loop |
| 2 | Fully connected neural network | Understand deep learning internals |
| 3 | PyTorch experiments | Build models with a mainstream framework |
| 4 | LLM deployment and APIs | Connect models to usable services |

A useful way to read each experiment is to ask four questions:

| Question | Purpose |
|---|---|
| What is the input data? | Clarify task boundaries |
| What does the model or algorithm do? | Connect code to theory |
| How is the result verified? | Define the outcome |
| Which part of the AI workflow does it represent? | Connect the experiment to real workflows |
