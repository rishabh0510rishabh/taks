import pandas as pd
import numpy as np
import random

def generate_housing_data(num_samples=1000):
    np.random.seed(42)
    
    # Features
    sizes = np.random.randint(500, 3500, size=num_samples) # Square footage
    rooms = np.random.randint(1, 6, size=num_samples) # Number of rooms
    
    # Location: 0=Rural, 1=Suburban, 2=Urban
    locations = np.random.choice(['Rural', 'Suburban', 'Urban'], size=num_samples)
    location_multipliers = {'Rural': 0.8, 'Suburban': 1.0, 'Urban': 1.2}
    
    prices = []
    
    for i in range(num_samples):
        base_price = (sizes[i] * 150) + (rooms[i] * 15000)
        loc_mult = location_multipliers[locations[i]]
        noise = np.random.randint(-20000, 20000)
        
        final_price = (base_price * loc_mult) + noise
        prices.append(int(final_price))
        
    df = pd.DataFrame({
        'Size_SqFt': sizes,
        'Bedrooms': rooms,
        'Location': locations,
        'Price': prices
    })
    
    return df

if __name__ == "__main__":
    print("Generating synthetic housing data...")
    df = generate_housing_data()
    df.to_csv('housing_data.csv', index=False)
    print("Data saved to housing_data.csv")
    print(df.head())
