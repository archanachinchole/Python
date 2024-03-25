import pandas as pd
import matplotlib.pyplot as plt

# Example time series data
dates = pd.date_range(start='2024-01-01', end='2024-03-01', freq='D')
data = [5, 8, 12, 9, 6, 10, 15, 18, 22, 19, 16, 20, 25, 28, 32, 29, 26, 30, 35, 38, 42, 39, 36, 40]

# Creating a DataFrame
df = pd.DataFrame({'Date': dates, 'Value': data})

# Plotting the time series
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Value'], marker='o', linestyle='-')
plt.title('Example Time Series')
plt.xlabel('Date')
plt.ylabel('Value')
plt.grid(True)
plt.show()
