# Define a function to find the largest element in a list
def find_largest_element(lst):
    if not lst:
        return None  # Return None if the list is empty
    largest = lst[0]  # Initialize the largest element with the first element of the list
    for num in lst:
        if num > largest:
            largest = num
    return largest

# Define a list of numbers
numbers = [5, 12, 9, 27, 6, 8]

# Call the find_largest_element function and store the result
largest_number = find_largest_element(numbers)

# Print the result
print("The largest number in the list is:", largest_number)
