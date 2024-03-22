def central_difference(f, x, h=1e-5):
    """
    Approximates the derivative of a function using the central difference method.
    
    :param f: The function whose derivative is to be approximated.
    :param x: The point at which to approximate the derivative.
    :param h: The step size for the approximation (optional, default is 1e-5).
    :return: The approximate derivative of the function at the given point.
    """
    return (f(x + h) - f(x - h)) / (2 * h)

# Example usage:
import math

# Define the function whose derivative is to be approximated
def f(x):
    return x**2 + math.sin(x)

# Choose a point at which to approximate the derivative
x = 1.0

# Approximate the derivative using the central difference method
approx_derivative = central_difference(f, x)

print("Approximate derivative at x =", x, ":", approx_derivative)
