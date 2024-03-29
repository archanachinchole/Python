def print_triangle_pattern(rows):
    for i in range(1, rows + 1):
        print(' '.join(['1'] * i))

# Number of rows in the pattern
num_rows = 8

# Call the function to print the pattern
print_triangle_pattern(num_rows)
