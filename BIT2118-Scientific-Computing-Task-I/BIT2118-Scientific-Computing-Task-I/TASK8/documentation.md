
# TASK 08: ITERATIVE METHODS FOR LINEAR SYSTEMS

## 1. Introduction

This task demonstrates two numerical techniques used to solve systems of linear equations: Jacobi Iteration and Gauss-Seidel Iteration.

The methods use repeated calculations to approximate the solution of a system of equations until the required accuracy is achieved.

## 2. Problem Statement

Solving large systems of linear equations can be computationally expensive using direct methods.

Iterative methods provide an alternative approach by repeatedly improving an estimated solution until it converges to an acceptable answer.

## 3. Objectives

- Implement the Jacobi Iteration method.
- Implement the Gauss-Seidel Iteration method.
- Solve a system of linear equations using both methods.
- Apply a specified convergence tolerance.
- Compare the results obtained from both methods.
- Verify the accuracy of the solutions.

## 4. Input Data

The coefficient matrix is:

A = [[10, -1, 2],
     [-1, 11, -1],
     [2, -1, 10]]

The constant vector is:

b = [6, 25, -11]

Additional parameters:

- Tolerance: 0.000001
- Maximum iterations: 100
- Initial solution: [0, 0, 0]

## 5. Mathematical Operations

### Jacobi Iteration

The Jacobi method calculates each new variable using values from the previous iteration.

### Gauss-Seidel Iteration

The Gauss-Seidel method uses newly calculated values immediately within the same iteration.

Both methods repeat the calculations until the difference between successive approximations is smaller than the specified tolerance.

## 6. Program Operations

The program performs the following operations:

1. Defines the coefficient matrix and constant vector.
2. Initializes the solution with zeros.
3. Executes Jacobi Iteration.
4. Executes Gauss-Seidel Iteration.
5. Checks the convergence tolerance.
6. Displays the calculated solutions and iteration counts.
7. Verifies the solutions using matrix multiplication.

## 7. Actual Output and Results

Both methods should converge to approximately:

x = [1, 2, -1]

The verification result should be approximately:

[6, 25, -11]

The two methods produce the same mathematical solution, although their iteration counts may differ.

## 8. Changing Input Parameters

The coefficient matrix, constant vector, tolerance and maximum number of iterations can be modified in the Python program.

For example, changing the tolerance from:

tolerance = 1e-6

to:

tolerance = 1e-8

requires greater accuracy before the program accepts a solution.

## 9. Real-World Applications

Iterative methods are applied in:

- Electrical circuit analysis.
- Engineering simulations.
- Scientific computing.
- Structural engineering.
- Heat transfer calculations.
- Economic modelling.

## 10. Interpretation

The Jacobi and Gauss-Seidel methods successfully approximate the solution of the given system of linear equations.

Both methods converge to approximately [1, 2, -1].

Gauss-Seidel often converges faster because it immediately uses updated values during calculations.

However, convergence depends on the properties of the coefficient matrix.

## 11. Conclusion

The task successfully demonstrates the implementation of Jacobi Iteration and Gauss-Seidel Iteration using Python.

The program illustrates how iterative numerical methods can solve systems of linear equations and how convergence tolerance helps control solution accuracy.
