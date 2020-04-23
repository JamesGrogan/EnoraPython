import math as math

# Function definitions
def trapezium_rule(f, m, x, a, b, n):
    """Implements the trapezium rule"""
    h = (b-a)/float(n)
    s = 0.5*(f(m, x, a) + f(m, x, b))
    for i in range(n):
        s = s + f(m, x, a + i*h)
    return h*s

def bessel(m, x, theta):
    """Holds the formula for the integral in the Bessel function"""
    return math.cos(m*theta - x*math.sin(theta))

def bessel_value(m, x):
    """Calculates the value of the Bessel function using the trapezium rule"""
    return (1 / math.pi) * trapezium_rule(bessel, m, x, 0, math.pi, 10000)