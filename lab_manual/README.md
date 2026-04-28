# HCIA-AI V4.0 Lab Manual Code

This directory organizes the lab code according to the HCIA-AI V4.0 Lab Framework. Larger experiments are kept in separate directories so datasets, model files, and environment notes can be added later.

## Structure

```text
lab_manual/
├── 01_machine_learning/
├── 02_deep_learning_fully_connected_nn_from_scratch/
├── 03_ai_development_framework_experiment/
└── 04_model_deployment_and_application_experiment/
```

## 1. Machine Learning Experiments

Directory:

```text
01_machine_learning/
```

Files:

```text
01_linear_regression_sklearn_pdf_original.py
02_linear_regression_expansion_numpy_gradient_descent_pdf_original.py
03_logistic_regression_classification_pdf_original.py
04_decision_tree_rule_based_classification_visualization_pdf_original.py
05_kmeans_unsupervised_clustering_pdf_original.py
```

## 2. Deep Learning Experiment

Directory:

```text
02_deep_learning_fully_connected_nn_from_scratch/
```

It contains the `MNIST/` project structure:

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

MNIST data files can be added later.

## 3. AI Development Framework Experiment

Directory:

```text
03_ai_development_framework_experiment/
├── 01_pytorch_basics/
├── 02_lenet_cifar10/
├── 03_resnet50_image_classification/
└── 04_textcnn_text_classification/
```

## 4. Model Deployment and Application Experiment

Directory:

```text
04_model_deployment_and_application_experiment/
├── 01_cli_based_llm_deployment/
└── 02_web_based_llm_deployment/
```

The web API examples are split into:

```text
01_health_check.py
02_requests_completion.py
03_openai_compatible_requests.py
04_openai_client_call.py
```
