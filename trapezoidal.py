def trapezoidal_rule(f, a, b, n):
    """
    Approximates the definite integral of a function using the trapezoidal rule.
    
    :param f: The function to be integrated.
    :param a: The lower limit of integration.
    :param b: The upper limit of integration.
    :param n: The number of trapezoids to use for approximation.
    :return: The approximate value of the definite integral.
    """
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b))  # Initial approximation
    
    for i in range(1, n):
        result += f(a + i * h)
    
    result *= h
    return result

# Example usage:
import math

# Define the function to be integrated
def f(x):
    return math.sin(x)

# Define the limits of integration
a = 0
b = math.pi

# Define the number of trapezoids
n = 1000

# Perform the integration
result = trapezoidal_rule(f, a, b, n)
print("Approximate integral using the trapezoidal rule:", result)
