
import numpy as np

# TASK 6: SOLUTION OF SYSTEMS OF LINEAR EQUATIONS

print("TASK 6: SOLUTION OF LINEAR EQUATIONS")
print("=" * 45)

# PART 1: Original assignment problem
# x = number of Type A servers
# y = number of Type B servers
#
# Type A uses 4 CPU units and 8 GB memory.
# Type B uses 2 CPU units and 12 GB memory.
# Total usage: 20 CPU units and 72 GB memory.

A = np.array([
    [4.0, 2.0],
    [8.0, 12.0]
])

b = np.array([20.0, 72.0])

solution = np.linalg.solve(A, b)

residual = b - A @ solution

print("\nPART 1: ORIGINAL SERVER PROBLEM")
print("Type A servers:", round(solution[0]))
print("Type B servers:", round(solution[1]))
print("Verification:", A @ solution)
print("Residual:", residual)
print("Residual norm:", np.linalg.norm(residual))


# PART 2: Change an input parameter
# Increase total CPU usage from 20 to 24.
# Increase memory usage from 72 GB to 80 GB.

b_changed = np.array([24.0, 80.0])

changed_solution = np.linalg.solve(A, b_changed)

print("\nPART 2: CHANGED INPUT VALUES")
print("Type A servers:", round(changed_solution[0]))
print("Type B servers:", round(changed_solution[1]))
print("Verification:", A @ changed_solution)


# PART 3: Related real-world application
# A factory uses two types of production machines.
#
# Machine A uses 2 labour hours and 3 kg of material.
# Machine B uses 4 labour hours and 2 kg of material.
#
# Total available resources:
# 16 labour hours and 12 kg of material.
#
# Find how many units of each machine type are used.

factory_A = np.array([
    [2.0, 4.0],
    [3.0, 2.0]
])

factory_b = np.array([16.0, 12.0])

factory_solution = np.linalg.solve(factory_A, factory_b)

print("\nPART 3: FACTORY RESOURCE ALLOCATION")
print("Machine A units:", factory_solution[0])
print("Machine B units:", factory_solution[1])
print("Verification:", factory_A @ factory_solution)
print("Residual:", factory_b - factory_A @ factory_solution)

print("\nPROGRAM COMPLETED SUCCESSFULLY.")
