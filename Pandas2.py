import pandas as pd

# Creating a DataFrame
data = [1, 2, 3, 7, 8, 9, 0, 1, 2]
df = pd.DataFrame(data, columns=['Values'])

# Data Exploration
print("First 3 rows:")
print(df.head(3))  # Display first 3 rows

print("\nData Information:")
print(df.info())   # Display information about the DataFrame

print("\nSummary Statistics:")
print(df.describe())  # Display summary statistics of numeric columns

# Data Cleaning and Preprocessing
print("\nAfter Dropping Duplicates:")
df.drop_duplicates(inplace=True)  # Drop duplicate rows
print(df)

# Indexing and Selection
print("\nSelecting Rows with Values > 3:")
print(df[df['Values'] > 3])  # Select rows where Values > 3

# Grouping and Aggregation (Not applicable in this case as there is only one column)
