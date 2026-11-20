
"""
TASK 19: NUMERICAL OPTIMIZATION
Application: Finding the minimum cost of cloud resource allocation.
"""

from scipy.optimize import minimize

# Cost function for allocating cloud resources
def cost_function(resources):
    cpu, memory = resources
    return (cpu - 8)**2 + (memory - 16)**2 + 10

# Initial resource allocation
initial_guess = [2, 4]

# Resource constraints
constraints = [
    {'type': 'ineq', 'fun': lambda x: x[0] - 1},
    {'type': 'ineq', 'fun': lambda x: x[1] - 2}
]

# Resource boundaries
bounds = [(1, 20), (2, 32)]

# Perform optimization
result = minimize(
    cost_function,
    initial_guess,
    method='SLSQP',
    bounds=bounds,
    constraints=constraints
)

print("--------------------------------")
print("TASK 19: NUMERICAL OPTIMIZATION")
print("--------------------------------")

if result.success:
    print(f"Optimal CPU allocation: {result.x[0]:.2f}")
    print(f"Optimal Memory allocation: {result.x[1]:.2f}")
    print(f"Minimum cost: {result.fun:.2f}")
    print("Optimization successful!")
else:
    print("Optimization failed:", result.message)
