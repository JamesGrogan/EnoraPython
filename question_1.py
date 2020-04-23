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