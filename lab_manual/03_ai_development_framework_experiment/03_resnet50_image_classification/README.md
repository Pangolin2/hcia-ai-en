# 03 ResNet-50 Image Classification

## 1. Scope

This directory corresponds to:

```text
1.4 ResNet-50 Image Classification
```

The script builds a ResNet-50 model with PyTorch and applies it to a five-class flower image classification task.

## 2. Workflow

```text
Prepare environment
  -> prepare flower dataset
  -> import PyTorch libraries
  -> define configuration
  -> define transforms and DataLoader
  -> define ResNet structure
  -> define loss and optimizer
  -> fit the model
  -> save the model
  -> evaluate accuracy
```

## 3. Dataset Layout

```text
flower_photos_train/
├── daisy
├── dandelion
├── roses
├── sunflowers
├── tulips
└── LICENSE.txt

flower_photos_test/
├── daisy
├── dandelion
├── roses
├── sunflowers
├── tulips
└── LICENSE.txt
```

## 4. Environment

| Item | Requirement |
|---|---|
| Python | 3.7 or later |
| PyTorch | 2.5 recommended by the guide |
| Device | CPU is used by default in the script |

## 5. Files

```text
03_resnet50_image_classification/
├── README.md
└── 03_resnet50_image_classification_pdf_original.py
```

The script follows the guide's Step 2 to Step 10 code and fixes text-extraction line breaks, indentation, and obvious syntax issues.

## 6. Notes

1. The guide path for `cfg.test_path` appears inconsistent with the test dataset description. This version uses `./flower_photos_test`.
2. The guide model filename contains a leading space and uses `renet50.pth`. This version keeps `renet50.pth` without the leading space.
3. The guide normalization constants are preserved for source alignment, although `transforms.ToTensor()` usually produces values in the range `0-1`.
4. Add `flower_photos_train/` and `flower_photos_test/` before running the script.

## 7. Run

```bash
cd lab_manual/03_ai_development_framework_experiment/03_resnet50_image_classification
python3 03_resnet50_image_classification_pdf_original.py
```
