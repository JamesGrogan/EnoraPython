import math as math
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import scipy.interpolate
from question_2_functions import *

# Plotting the Bessel functions
x_values = [[], [], []] # List of three empty lists to store the x values of the Bessel function from m=0 to m=2. Each list will become a list of 0 to 20 inclusive.
bessel_values = [[], [], []] # List of three empty lists to store the values of the Bessel function from m=0 to m=2. Each list contains the Bessel function value from x=0 to x=20.

for m in range(0, 3, 1): # Loops through m values
    for x in range(0, 21, 1): # Loops through x values
        x_values[m].append(x)
        bessel_values[m].append(bessel_value(m, x)) # Calculates the value of the Bessel function and adds it to the list

for element in range(len(x_values)):
    # Interpolating to make lines smooth
    x_values_new = np.linspace(x_values[element][0], x_values[element][-1], 300)
    a_BSpline = sp.interpolate.make_interp_spline(x_values[element], bessel_values[element])
    bessel_values_new = a_BSpline(x_values_new)
    plt.plot(x_values_new, bessel_values_new, label=("m = " + str(element)))
plt.title("Bessel functions for different values of m")
plt.ylabel("Bessel function value")
plt.xlabel("x")
plt.legend()
plt.show()