
import numpy as np

# Sales data: each row represents a product
# Columns: Product price, Quantity sold, Total sales
sales_data = np.array([
    [100, 5, 500],
    [200, 3, 600],
    [150, 4, 600]
])

# Extract the product prices (first column)
prices = sales_data[:, 0]

# Calculate the average price
average_price = np.mean(prices)

# Display the result
print("Product prices:", prices)
print("Average price:", average_price)
