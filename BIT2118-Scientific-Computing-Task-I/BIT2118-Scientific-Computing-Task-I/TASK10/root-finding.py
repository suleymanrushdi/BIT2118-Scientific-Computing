
# Task 10: Bisection and Fixed-Point Iteration

def function(x):
    return x**3 - x - 2


# Bisection Method
def bisection(a, b, tolerance=0.0001):
    if function(a) * function(b) >= 0:
        return None

    while abs(b - a) > tolerance:
        c = (a + b) / 2

        if function(c) == 0:
            return c
        elif function(a) * function(c) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2


# Fixed-Point Iteration
def g(x):
    return (x + 2)**(1/3)


def fixed_point(x0, tolerance=0.0001, max_iterations=100):
    for i in range(max_iterations):
        x1 = g(x0)

        if abs(x1 - x0) < tolerance:
            return x1

        x0 = x1

    return x0


# Main Program
print("TASK 10: ROOT FINDING METHODS")

root1 = bisection(1, 2)
root2 = fixed_point(1.5)

print("\nBisection Method")
print("Root:", root1)

print("\nFixed-Point Iteration")
print("Root:", root2)
