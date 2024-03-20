import pandas as pd

# Create a 3x3 matrix
matrix_data = [
    [1, 2, 3],
    [4, 4, 5],
    [6, 7, 5]
]

# Create a DataFrame from the matrix
df = pd.DataFrame(matrix_data, columns=['Column1', 'Column2', 'Column3'])

# Display the DataFrame
print("DataFrame created from the matrix:")
print(df)

# Accessing specific elements in the DataFrame
print("\nElement at row 2, column 3:", df.at[1, 'Column3'])

# Summing values along columns and adding a new row for totals
df.loc['Total'] = df.sum()

# Display the DataFrame with totals
print("\nDataFrame with row totals:")
print(df)
