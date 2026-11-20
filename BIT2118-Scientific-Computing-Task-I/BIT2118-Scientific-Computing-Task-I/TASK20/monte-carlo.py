
"""
TASK 20: RANDOM NUMBERS AND MONTE CARLO METHODS
Application: Estimating the value of Pi using random numbers.
"""

import random
import math

# Number of random points
total_points = 100000

# Count points inside the circle
inside_circle = 0

# Generate random points
for _ in range(total_points):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    # Check whether point is inside the circle
    if x**2 + y**2 <= 1:
        inside_circle += 1

# Estimate Pi
pi_estimate = 4 * inside_circle / total_points

# Calculate error
error = abs(math.pi - pi_estimate)

print("--------------------------------")
print("TASK 20: MONTE CARLO METHODS")
print("--------------------------------")

print(f"Total random points: {total_points}")
print(f"Points inside circle: {inside_circle}")
print(f"Estimated value of Pi: {pi_estimate:.6f}")
print(f"Actual value of Pi: {math.pi:.6f}")
print(f"Estimation error: {error:.6f}")

print("Monte Carlo simulation completed!")
