# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to find the factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Main code
start = 1
end = 20

print(f"Prime numbers between {start} and {end} and their factorials:")

for num in range(start, end + 1):
    if is_prime(num):
        print(f"Prime: {num}, Factorial: {factorial(num)}")
