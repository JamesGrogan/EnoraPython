import math as math
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import scipy.interpolate

# QUESTION ONE

# Defining constants
gravitational_constant = 6.6741E-11
earth_radius = 6371.0
moon_radius = 1737.1
earth_mass = 5.9722E24
moon_mass = 7.3420E22
earth_moon_distance = 3.8440E8
angular_velocity = 2.6617E-6

# x0 and x1 are two initial approximations for the root of f(x) = 0
def secant_method(f, x0, x1, iterations):
    for i in range(iterations):
        x2 = x1 - (f(x1) * (x1 - x0) / float(f(x1) - f(x0)))
        x0, x1 = x1, x2
    return x2

def lagrange_point_one(x):
    return (((gravitational_constant * earth_mass) / x ** 2) - ((gravitational_constant * moon_mass) / ((earth_moon_distance - x) ** 2))) / (angular_velocity ** 2)

root = secant_method(lagrange_point_one, 3.1E8, 3.3E8, 11)
print("Calculated lagrange point is: " + str(format(root, '.5g'))) # format() converts display output to 5 significant figures
#print("Actual lagrange point is: " + str(format(earth_moon_distance * 0.8403997, '.5g')))


# QUESTION TWO

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

# Plotting the Bessel functions
x_values = [[], [], []] # List of three empty lists to store the x values of the Bessel function from m=0 to m=2. Each list will become a list of 0 to 20 inclusive.
bessel_values = [[], [], []] # List of three empty lists to store the values of the Bessel function from m=0 to m=2. Each list contains the Bessel function value from x=0 to x=20.

for m in range(0, 3, 1): # Loops through m values
    for x in range(0, 21, 1): # Loops through x values
        x_values[m].append(x)
        bessel_values[m].append(bessel_value(m, x)) # Calculates the value of the Bessel function and adds it to the list


for element in range(len(x_values)):
    x_values_new = np.linspace(x_values[element][0], x_values[element][-1], 300)
    a_BSpline = sp.interpolate.make_interp_spline(x_values[element], bessel_values[element])
    bessel_values_new = a_BSpline(x_values_new)
    plt.plot(x_values_new, bessel_values_new, label=("m = " + str(element)))
plt.title("Bessel functions for different values of m")
plt.ylabel("Bessel function value")
plt.xlabel("x")
plt.legend()
plt.show()
