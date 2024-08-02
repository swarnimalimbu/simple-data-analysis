import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('/Users/ingshaphombohang/Desktop/data.csv')

# Print the first few rows of the dataframe
print("Data Overview:")
print(df.head())

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Value'], marker='o')
plt.title('Sample Data Plot')
plt.xlabel('Date')
plt.ylabel('Value')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('plot.png')
plt.show()
