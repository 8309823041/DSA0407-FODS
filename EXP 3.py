
import numpy as np

# House data: Bedrooms, Square Footage, Sale Price
house_data = np.array([
    [3, 1200, 200000],
    [5, 1800, 350000],
    [4, 1500, 280000],
    [6, 2200, 450000],
    [5, 2000, 400000]
])

# Select houses with more than 4 bedrooms
selected_houses = house_data[house_data[:, 0] > 4]

# Extract sale prices (third column)
sale_prices = selected_houses[:, 2]

# Calculate average sale price
average_price = np.mean(sale_prices)

# Display results
print("Houses with more than 4 bedrooms:")
print(selected_houses)

print("\nSale prices:", sale_prices)
print("Average sale price:", average_price)
