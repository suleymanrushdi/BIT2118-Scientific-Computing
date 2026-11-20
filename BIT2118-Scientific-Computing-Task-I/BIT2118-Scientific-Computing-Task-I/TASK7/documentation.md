
# TASK 07: GAUSSIAN ELIMINATION AND LU DECOMPOSITION

## 1. Introduction

This task implements two numerical methods used to solve systems of linear equations: Gaussian Elimination and LU Decomposition.

The program uses Python and NumPy to perform matrix calculations and obtain solutions.

## 2. Problem Statement

Systems of linear equations are commonly used in scientific and engineering problems. Solving these equations manually can be time-consuming, especially when dealing with large matrices.

This program demonstrates how Gaussian Elimination and LU Decomposition can be used to solve a system of three linear equations.

## 3. Objectives

- Implement Gaussian Elimination.
- Perform LU Decomposition.
- Solve linear equations using forward and backward substitution.
- Compare the solutions obtained using both methods.
- Verify the accuracy of the calculated results.

## 4. Input Data

The coefficient matrix is:

A = [[2, 1, -1],
     [-3, -1, 2],
     [-2, 1, 2]]

The constant vector is:

b = [8, -11, -3]

## 5. Operations Performed

The program performs the following operations:

1. Accepts the coefficient matrix and constant vector.
2. Applies Gaussian Elimination to transform the system into an upper triangular form.
3. Uses back substitution to calculate the unknown variables.
4. Decomposes the coefficient matrix into lower and upper triangular matrices.
5. Uses forward and backward substitution to solve the system using LU Decomposition.
6. Verifies the solution by multiplying the coefficient matrix by the calculated solution.

## 6. Actual Output

The expected solution from Gaussian Elimination is:

x = [2, 3, -1]

The LU Decomposition method produces the same solution:

x = [2, 3, -1]

The verification produces:

[8, -11, -3]

This confirms that both methods produce the correct solution.

## 7. Changing the Input

The input values can be changed by modifying matrix A and vector b in the Python source file.

For example, the constant vector can be changed from:

b = [8, -11, -3]

to:

b = [10, -5, 4]

The program will calculate a new solution for the modified system, provided the matrix is suitable for the implemented methods.

## 8. Real-World Applications

Gaussian Elimination and LU Decomposition are used in:

- Engineering calculations.
- Scientific simulations.
- Electrical circuit analysis.
- Structural analysis.
- Economic modelling.
- Computer graphics and numerical computing.

## 9. Assumptions and Limitations

- The coefficient matrix must be square.
- The matrix must have non-zero pivots in the implemented elimination order.
- The system must have a unique solution.
- NumPy must be installed before running the program.
- The implementation does not include partial pivoting.

## 10. Interpretation

The program demonstrates that Gaussian Elimination and LU Decomposition can independently solve the same system of linear equations.

Both methods produce the solution [2, 3, -1].

The verification step confirms that the calculated values satisfy the original equations.

## 11. Conclusion

The task successfully demonstrates two important numerical methods for solving systems of linear equations.

It also illustrates the importance of matrix decomposition, substitution techniques and solution verification in scientific computing.
