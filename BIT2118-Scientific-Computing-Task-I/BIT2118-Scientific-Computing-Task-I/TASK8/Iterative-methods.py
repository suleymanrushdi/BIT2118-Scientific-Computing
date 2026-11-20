
# TASK 08: ITERATIVE METHODS FOR LINEAR SYSTEMS
# Scientific Computing Assignment

import numpy as np


def jacobi_method(A, b, tolerance=1e-6, max_iterations=100):
    """Solve a linear system using Jacobi iteration."""

    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)

    n = len(b)
    x = np.zeros(n)

    for iteration in range(max_iterations):
        x_new = np.zeros(n)

        for i in range(n):
            if abs(A[i, i]) < 1e-10:
                raise ValueError("Zero diagonal element encountered.")

            sum_value = sum(
                A[i, j] * x[j]
                for j in range(n) if j != i
            )

            x_new[i] = (b[i] - sum_value) / A[i, i]

        if np.linalg.norm(x_new - x, ord=np.inf) < tolerance:
            return x_new, iteration + 1

        x = x_new

    raise ValueError("Jacobi method did not converge.")


def gauss_seidel_method(A, b, tolerance=1e-6,
                        max_iterations=100):
    """Solve a linear system using Gauss-Seidel iteration."""

    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)

    n = len(b)
    x = np.zeros(n)

    for iteration in range(max_iterations):
        x_old = x.copy()

        for i in range(n):
            if abs(A[i, i]) < 1e-10:
                raise ValueError("Zero diagonal element encountered.")

            sum_value = sum(
                A[i, j] * x[j]
                for j in range(n) if j != i
            )

            x[i] = (b[i] - sum_value) / A[i, i]

        if np.linalg.norm(x - x_old, ord=np.inf) < tolerance:
            return x, iteration + 1

    raise ValueError("Gauss-Seidel method did not converge.")


# Main program
A = [
    [10, -1, 2],
    [-1, 11, -1],
    [2, -1, 10]
]

b = [6, 25, -11]

tolerance = 1e-6
max_iterations = 100

print("TASK 08: ITERATIVE METHODS FOR LINEAR SYSTEMS")
print("=" * 55)

print("\nCoefficient Matrix A:")
print(np.array(A))

print("\nConstant Vector b:")
print(np.array(b))

# Jacobi Method
jacobi_solution, jacobi_iterations = jacobi_method(
    A, b, tolerance, max_iterations
)

print("\nSolution Using Jacobi Method:")
print(jacobi_solution)
print("Number of iterations:", jacobi_iterations)

# Gauss-Seidel Method
gs_solution, gs_iterations = gauss_seidel_method(
    A, b, tolerance, max_iterations
)

print("\nSolution Using Gauss-Seidel Method:")
print(gs_solution)
print("Number of iterations:", gs_iterations)

# Verification
print("\nVerification Using Jacobi:")
print(np.dot(A, jacobi_solution))

print("\nVerification Using Gauss-Seidel:")
print(np.dot(A, gs_solution))

print("\nTask 08 completed successfully.")
