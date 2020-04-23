import math as math
import matplotlib.pyplot as plt
from question_2_functions import *

wavelength = 0.6 # Using micrometers as the unit to prevent floating point errors with very small numbers
r_list = []
intensity_list = []

for r in range(-25, 26, 1):
    if r == 0: # To avoid division by zero error
        r_list.append(0)
        intensity_list.append(1)
        continue
    r_list.append(r)
    x = (2*math.pi / wavelength) * (r / 20) * 1 # R/2a is 10 therefore made R = 20 and a = 1
    intensity = ((2 * bessel_value(1, x)) / x) ** 2 # Assuming I0 is 1
    intensity_list.append(intensity)

plt.plot(r_list, intensity_list)
plt.show()