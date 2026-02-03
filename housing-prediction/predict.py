import joblib
import pandas as pd
import sys

def predict_price(size, bedrooms, location):
    try:
        model = joblib.load('house_price_model.pkl')
    except FileNotFoundError:
        print("Model not found. Please run train_model.py first.")
        return

    input_data = pd.DataFrame({
        'Size_SqFt': [size],
        'Bedrooms': [bedrooms],
        'Location': [location]
    })

    prediction = model.predict(input_data)[0]
    return prediction

if __name__ == "__main__":
    print("--- House Price Predictor ---")
    if len(sys.argv) > 1:
        # Manual Mode not implemented for argv simplicity, using interactive
        pass
    
    try:
        size = float(input("Enter Size (SqFt): "))
        beds = int(input("Enter Bedrooms: "))
        print("Locations: Rural, Suburban, Urban")
        loc = input("Enter Location: ").strip()
        
        if loc not in ['Rural', 'Suburban', 'Urban']:
            print("Invalid location. Defaulting to Suburban.")
            loc = 'Suburban'
            
        price = predict_price(size, beds, loc)
        print(f"\nEstimated Price: ${price:,.2f}")
    except ValueError:
        print("Invalid input.")
    except Exception as e:
        print(f"An error occurred: {e}")
