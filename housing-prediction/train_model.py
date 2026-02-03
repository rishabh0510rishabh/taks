import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

def train():
    try:
        # Load Data
        df = pd.read_csv('housing_data.csv')
    except FileNotFoundError:
        print("Error: housing_data.csv not found. Run generate_data.py first.")
        return

    X = df[['Size_SqFt', 'Bedrooms', 'Location']]
    y = df['Price']

    # Preprocessing for categorical data (Location)
    preprocessor = ColumnTransformer(
        transformers=[
            ('cat', OneHotEncoder(), ['Location'])
        ],
        remainder='passthrough'
    )

    # Pipeline
    model = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('regressor', LinearRegression())
    ])

    # Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train
    print("Training model...")
    model.fit(X_train, y_train)

    # Evaluate
    preds = model.predict(X_test)
    mae = mean_absolute_error(y_test, preds)
    r2 = r2_score(y_test, preds)

    print(f"Model Trained.")
    print(f"Mean Absolute Error: ${mae:,.2f}")
    print(f"R2 Score: {r2:.4f}")

    # Save
    joblib.dump(model, 'house_price_model.pkl')
    print("Model saved to house_price_model.pkl")

if __name__ == "__main__":
    train()
