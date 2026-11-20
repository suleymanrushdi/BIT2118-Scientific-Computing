
# TASK 07: GAUSSIAN ELIMINATION AND LU DECOMPOSITION
# Scientific Computing Assignment

import numpy as np


def gaussian_elimination(A, b):
    """Solve a linear system using Gaussian elimination."""

    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)

    n = len(b)
    augmented = np.column_stack((A, b))

    # Forward elimination
    for i in range(n):
        if abs(augmented[i, i]) < 1e-10:
            raise ValueError("Zero pivot encountered.")

        for j in range(i + 1, n):
            factor = augmented[j, i] / augmented[i, i]
            augmented[j, i:] -= factor * augmented[i, i:]

    # Back substitution
    x = np.zeros(n)

    for i in range(n - 1, -1, -1):
        x[i] = (
            augmented[i, -1]
            - np.dot(augmented[i, i + 1:n], x[i + 1:n])
        ) / augmented[i, i]

    return x


def lu_decomposition(A):
    """Decompose matrix A into lower and upper triangular matrices."""

    A = np.array(A, dtype=float)
    n = len(A)

    L = np.eye(n)
    U = np.zeros((n, n))

    for i in range(n):
        # Calculate upper triangular matrix
        for k in range(i, n):
            U[i, k] = A[i, k] - np.dot(L[i, :i], U[:i, k])

        # Calculate lower triangular matrix
        for k in range(i + 1, n):
            if abs(U[i, i]) < 1e-10:
                raise ValueError("Zero pivot encountered.")

            L[k, i] = (
                A[k, i] - np.dot(L[k, :i], U[:i, i])
            ) / U[i, i]

    return L, U


def solve_lu(L, U, b):
    """Solve Ax=b using LU decomposition."""

    n = len(b)
    y = np.zeros(n)
    x = np.zeros(n)

    # Forward substitution: Ly = b
    for i in range(n):
        y[i] = b[i] - np.dot(L[i, :i], y[:i])

    # Back substitution: Ux = y
    for i in range(n - 1, -1, -1):
        if abs(U[i, i]) < 1e-10:
            raise ValueError("Zero pivot encountered.")

        x[i] = (
            y[i] - np.dot(U[i, i + 1:], x[i + 1:])
        ) / U[i, i]

    return x


# Main program
A = [
    [2, 1, -1],
    [-3, -1, 2],
    [-2, 1, 2]
]

b = [8, -11, -3]

print("TASK 07: GAUSSIAN ELIMINATION AND LU DECOMPOSITION")
print("=" * 55)

print("\nCoefficient Matrix A:")
print(np.array(A))

print("\nConstant Vector b:")
print(np.array(b))

# Gaussian Elimination
gaussian_solution = gaussian_elimination(A, b)

print("\nSolution using Gaussian Elimination:")
print(gaussian_solution)

# LU Decomposition
L, U = lu_decomposition(A)

print("\nLower Triangular Matrix (L):")
print(L)

print("\nUpper Triangular Matrix (U):")
print(U)

# Solve using LU
lu_solution = solve_lu(L, U, np.array(b, dtype=float))

print("\nSolution using LU Decomposition:")
print(lu_solution)

# Verification
print("\nVerification (A multiplied by x):")
print(np.dot(A, gaussian_solution))

print("\nTask 07 completed successfully.")
