#!/usr/bin/env python3
"""
HCIA-AI V4.0 Machine Learning Lab
Experiment 1: Linear Regression with scikit-learn

This script follows the Lab Guide example:
1. Build a small house area/price dataset.
2. Visualize the raw data.
3. Train a LinearRegression model.
4. Print slope and intercept.
5. Visualize the fitted line.
6. Predict the price for a test sample.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

try:
    import matplotlib.pyplot as plt
    import numpy as np
    from sklearn.linear_model import LinearRegression
except ModuleNotFoundError as exc:
    missing_package = exc.name
    install_name = "scikit-learn" if missing_package == "sklearn" else missing_package
    print(
        f"Missing dependency: {missing_package}\n"
        f"Install it with: python3 -m pip install {install_name}",
        file=sys.stderr,
    )
    raise SystemExit(1) from exc


def build_dataset() -> tuple[np.ndarray, np.ndarray]:
    """Create the house area and price dataset from the lab guide."""
    x = np.array([121, 125, 131, 141, 152, 161]).reshape(-1, 1)
    y = np.array([300, 350, 425, 405, 496, 517])
    return x, y


def train_model(x: np.ndarray, y: np.ndarray) -> LinearRegression:
    """Train a simple linear regression model."""
    model = LinearRegression()
    model.fit(x, y)
    return model


def predict_price(model: LinearRegression, area: float) -> float:
    """Predict the house price for a given area."""
    test_x = np.array([[area]])
    return float(model.predict(test_x)[0])


def plot_dataset(x: np.ndarray, y: np.ndarray, output_path: Path) -> None:
    """Save a scatter plot of the original dataset."""
    plt.figure(figsize=(7, 5))
    plt.scatter(x, y, color="#2563eb", label="Training samples")
    plt.xlabel("area")
    plt.ylabel("price")
    plt.title("House Area and Price Dataset")
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()


def plot_fitted_model(
    x: np.ndarray,
    y: np.ndarray,
    model: LinearRegression,
    output_path: Path,
) -> None:
    """Save a scatter plot with the fitted linear regression line."""
    y_pred = model.predict(x)

    plt.figure(figsize=(7, 5))
    plt.scatter(x, y, color="#2563eb", label="Training samples")
    plt.plot(x, y_pred, color="#dc2626", linewidth=2, label="Fitted line")
    plt.xlabel("area")
    plt.ylabel("price")
    plt.title("Linear Regression Fitted Result")
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run HCIA-AI V4.0 Experiment 1: Linear Regression with sklearn."
    )
    parser.add_argument(
        "--test-area",
        type=float,
        default=130.0,
        help="House area used for prediction. Default: 130.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("lab_manual/outputs"),
        help="Directory used to save generated figures. Default: lab_manual/outputs.",
    )
    parser.add_argument(
        "--show",
        action="store_true",
        help="Show the fitted plot window after saving figures.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    x, y = build_dataset()
    model = train_model(x, y)

    slope = model.coef_[0]
    intercept = model.intercept_
    predicted_price = predict_price(model, args.test_area)

    dataset_plot = args.output_dir / "linear_regression_dataset.png"
    fitted_plot = args.output_dir / "linear_regression_fitted.png"
    plot_dataset(x, y, dataset_plot)
    plot_fitted_model(x, y, model, fitted_plot)

    print("Experiment 1: Linear Regression with scikit-learn")
    print(f"Dataset x shape: {x.shape}")
    print(f"Dataset y shape: {y.shape}")
    print(f"Slope: {slope:.8f}")
    print(f"Intercept: {intercept:.8f}")
    print(f"Prediction input area: {args.test_area:g}")
    print(f"Predicted price: {predicted_price:.8f}")
    print(f"Saved dataset plot: {dataset_plot}")
    print(f"Saved fitted plot: {fitted_plot}")

    if args.show:
        plt.figure(figsize=(7, 5))
        plt.scatter(x, y, color="#2563eb", label="Training samples")
        plt.plot(x, model.predict(x), color="#dc2626", linewidth=2, label="Fitted line")
        plt.xlabel("area")
        plt.ylabel("price")
        plt.title("Linear Regression Fitted Result")
        plt.legend()
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    main()
