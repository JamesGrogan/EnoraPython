# x0 and x1 are two initial approximations for the root of f(x) = 0
def secant_method(f, x0, x1, iterations):
    for i in range(iterations):
        x2 = x1 - f(x1) * (x1 - x0) / float(f(x1) - f(x0))
        x0, x1 = x1, x2
    return x2

def example_function(x):
    return x**2 - 612

root = secant_method(example_function, 10, 30, 5)

print(root)