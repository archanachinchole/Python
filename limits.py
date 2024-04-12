import sympy as sp
from scipy.integrate import quad

# Define the symbol and the function
x = sp.Symbol('x')
f = x**2 + 3*x + 5

# Define the limits for numerical integration
a = 0
b = 1

# Symbolic integration
integral_symbolic = sp.integrate(f, x)

# Numerical integration
def f_numeric(x):
    return x**2 + 3*x + 5

integral_numeric, error = quad(f_numeric, a, b)

print("Symbolic integral:", integral_symbolic)
print("Numerical integral (from {} to {}): {}".format(a, b, integral_numeric))
