# TASK 6: SOLUTION OF SYSTEMS OF LINEAR EQUATIONS

## 1. Introduction

A system of linear equations consists of two or more equations involving unknown variables. In scientific computing, NumPy provides tools for solving these equations efficiently.

This task demonstrates how to solve simultaneous linear equations using the `numpy.linalg.solve()` function.

## 2. Problem Statement

A company operates two types of servers. Type A servers consume 4 CPU units and 8 GB of memory, while Type B servers consume 2 CPU units and 12 GB of memory.

The total observed consumption is 20 CPU units and 72 GB of memory. The objective is to determine the number of each server type.

## 3. Objectives

- Understand systems of linear equations.
- Represent equations using matrices.
- Solve equations using NumPy.
- Verify solutions through matrix multiplication.
- Apply linear equations to another real-world problem.

## 4. Input Values

The original equations are:

4x + 2y = 20

8x + 12y = 72

Where:
- x represents the number of Type A servers.
- y represents the number of Type B servers.

The matrix representation is:

A = [[4, 2], [8, 12]]

b = [20, 72]

## 5. Mathematical Operations Performed

The program solves the matrix equation:

Ax = b

It uses:

`np.linalg.solve(A, b)`

The solution is then verified using:

`A @ solution`

The residual is calculated by subtracting the calculated resource usage from the original resource totals.

## 6. Technologies Used

- Python programming language.
- NumPy library.
- Visual Studio Code.

## 7. Original Program Output and Interpretation

The expected solution is:

- Type A servers = 3
- Type B servers = 4

This means the company has three Type A servers and four Type B servers.

The verification produces the original resource totals: 20 CPU units and 72 GB of memory. The residual should be approximately zero, showing that the solution is correct.

## 8. Changing an Input Parameter

The original resource totals are changed from:

- CPU: 20 to 24 units.
- Memory: 72 GB to 80 GB.

The new equations are:

4x + 2y = 24

8x + 12y = 80

The new solution is:

- Type A servers = 4
- Type B servers = 4

This demonstrates that changing the available resource totals changes the solution.

## 9. Related Real-World Application: Factory Resource Allocation

### Problem

A factory uses two types of production machines. Management wants to determine the number of units of each type that can be operated using the available labour hours and raw materials.

### Assumptions

- Machine A uses 2 labour hours and 3 kg of material.
- Machine B uses 4 labour hours and 2 kg of material.
- The factory has 16 labour hours and 12 kg of material available.
- The resource usage is assumed to be fixed for each machine.

### Input Data

The equations are:

2x + 4y = 16

3x + 2y = 12

Where:
- x represents Machine A units.
- y represents Machine B units.

### Mathematical Operation

The equations are represented using a coefficient matrix and a resource vector. NumPy's `np.linalg.solve()` function is used to calculate the unknown values.

### Expected Output

- Machine A units = 2
- Machine B units = 3

### Interpretation

The factory can operate two Machine A units and three Machine B units using exactly 16 labour hours and 12 kg of material.

This demonstrates how systems of linear equations can support resource allocation and production planning.

## 10. Conclusion

This task demonstrated how systems of linear equations can be solved using Python and NumPy. The program used matrix representation, the `np.linalg.solve()` function and matrix multiplication to verify results.

The factory application further demonstrated how the same mathematical concept can solve practical resource allocation problems.