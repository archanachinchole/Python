# Define a function to find the smallest element in a list
def find_smallest_element(lst):
    if not lst:
        return None  # Return None if the list is empty
    smallest = lst[0]  # Initialize the smallest element with the first element of the list
    for num in lst:
        if num < smallest:
            smallest = num
    return smallest

# Define a list of numbers
numbers = [5, 12, 9, 27, 6, 8]

# Call the find_smallest_element function and store the result
smallest_number = find_smallest_element(numbers)

# Print the result
print("The smallest number in the list is:", smallest_number)
