# Housing Price Predictor

A Machine Learning project that predicts house prices based on features like size, number of bedrooms, and location.

## Overview
This project demonstrates the use of Linear Regression to solve a regression problem. It includes scripts for data generation, model training, and prediction.

## Files
-   `generate_data.py`: Creates a synthetic dataset (`housing_data.csv`).
-   `train_model.py`: Trains the model and saves it as `house_price_model.pkl`.
-   `predict.py`: User-friendly script to get price estimates.

## Usage

1.  **Install Requirements:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Generate Data:**
    ```bash
    python generate_data.py
    ```

3.  **Train Model:**
    ```bash
    python train_model.py
    ```

4.  **Predict Price:**
    ```bash
    python predict.py
    ```
    *Follow the on-screen prompts to enter house details.*
