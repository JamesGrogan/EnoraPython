import math as math
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import scipy.interpolate
from question_2_functions import *

wavelength = 0.6 # Using micrometers as the unit to prevent floating point errors with very small numbers
r_values = []
intensity_values = []

for r in range(-25, 26, 1):
    if r == 0: # To avoid division by zero error
        r_values.append(0)
        intensity_values.append(1)
        continue
    r_values.append(r)
    x = (2*math.pi / wavelength) * (r / 20) * 1 # R/2a is 10 therefore made R = 20 and a = 1
    intensity = ((2 * bessel_value(1, x)) / x) ** 2 # Assuming I0 is 1
    intensity_values.append(intensity)

# Smoothing line
r_values_new = np.linspace(r_values[0], r_values[-1], 300)
a_BSpline = sp.interpolate.make_interp_spline(r_values, intensity_values)
intensity_values_new = a_BSpline(r_values_new)

# Plotting
plt.plot(r_values_new, intensity_values_new)
plt.title("Diffraction pattern for a circular lens with focal ratio = 10. Lambda = 0.6 micrometres")
plt.ylabel("Relative intensity")
plt.xlabel("Radius (micrometres)")
plt.show()