
# TASK 5: MATRIX ALGEBRA AND MATRIX OPERATIONS

## 1. Introduction

Matrix algebra is an important area of scientific computing that deals with mathematical operations involving matrices.

A matrix is a rectangular arrangement of numbers organized in rows and columns.

Matrices are used in computer graphics, robotics, machine learning, electrical engineering and solving systems of equations.

Python's NumPy library provides functions for performing matrix operations efficiently.

## 2. Problem Statement

A computer graphics program needs to rotate and scale a two-dimensional square object.

The coordinates of the square are represented using a matrix. Rotation and scaling matrices are created and combined to transform the original coordinates.

The program uses matrix multiplication to calculate the new positions of the square's corners.

## 3. Objectives

The objectives of this task are:

- To understand matrices and matrix algebra.
- To create matrices using NumPy.
- To perform matrix multiplication.
- To understand rotation and scaling transformations.
- To calculate the determinant of a matrix.
- To apply matrix operations to a real-world problem.

## 4. Input Values

The program uses four coordinate points representing the corners of a square:

(0, 0), (1, 0), (1, 1) and (0, 1).

The rotation angle is 45 degrees.

The scaling factors are:

- Horizontal scaling: 2.0
- Vertical scaling: 1.5

The program also changes the rotation angle to 90 degrees to demonstrate the effect of changing an input parameter.

## 5. Mathematical Concepts and Operations

### A. Matrix Representation

The four square coordinates are represented as a matrix:

```text
[[0, 0],
 [1, 0],
 [1, 1],
 [0, 1]]
```

Each row represents one point with its x and y coordinates.

### B. Rotation Matrix

A rotation matrix is used to rotate coordinates through a specified angle.

The formula is:

```text
R = [[cos(theta), -sin(theta)],
     [sin(theta),  cos(theta)]]
```

Where theta represents the rotation angle.

### C. Scaling Matrix

A scaling matrix changes the size of an object.

The scaling matrix used is:

```text
S = [[2.0, 0.0],
     [0.0, 1.5]]
```

This doubles the horizontal coordinate and increases the vertical coordinate by a factor of 1.5.

### D. Matrix Multiplication

The rotation and scaling matrices are combined using matrix multiplication:

T = R × S

The transformed coordinates are calculated using:

New Points = Original Points × T Transpose

In Python, the `@` operator performs matrix multiplication.

### E. Determinant

The determinant is a numerical value calculated from a square matrix.

For a 2 × 2 matrix:

```text
A = [[a, b],
     [c, d]]
```

The determinant is:

Det(A) = (a × d) - (b × c)

The determinant helps determine whether a square matrix has an inverse.

A non-zero determinant indicates that the matrix is invertible.

## 6. Python Library Used

The program uses NumPy.

It is imported using:

`import numpy as np`

The following NumPy functions and operations are used:

- `np.array()` – creates matrices.
- `np.deg2rad()` – converts degrees into radians.
- `np.cos()` – calculates cosine.
- `np.sin()` – calculates sine.
- `np.linalg.det()` – calculates the determinant.
- `@` – performs matrix multiplication.
- `np.round()` – rounds numerical results.

## 7. Expected Program Output

The first part should produce approximately:

```text
Original points:
[[0. 0.]
 [1. 0.]
 [1. 1.]
 [0. 1.]]

Transformation matrix:
[[ 1.4142 -1.0607]
 [ 1.4142  1.0607]]

Transformed points:
[[ 0.      0.    ]
 [ 1.4142  1.4142]
 [ 0.3536  2.4749]
 [-1.0607  1.0607]]

Determinant: 3.0
```

After changing the rotation angle to 90 degrees:

```text
New rotation angle: 90 degrees

New transformed points:
[[ 0.   0. ]
 [ 0.   2. ]
 [-1.5  2. ]
 [-1.5  0. ]]
```

The program also displays the original and transformed robot positions in Part 3.

## 8. Interpretation of Results

The program successfully transforms the original square coordinates using matrix multiplication.

The rotation matrix changes the orientation of the square, while the scaling matrix changes its dimensions.

The determinant of the transformation matrix is 3.0.

Since the determinant is non-zero, the transformation matrix is invertible.

The results demonstrate how matrix algebra can be used to manipulate two-dimensional objects in computer graphics.

## 9. Changing an Input Parameter

The original rotation angle is 45 degrees.

The program is modified by changing the rotation angle from 45 degrees to 90 degrees.

After changing the angle, the transformed coordinates also change.

This happens because the rotation matrix uses the angle to calculate the new positions of the object's points.

The square is therefore rotated through a larger angle while maintaining the same scaling factors.

This demonstrates how changing a parameter affects the results of matrix operations.

## 10. Related Real-World Application

### Robot Movement in a Warehouse

Robots are commonly used in warehouses to move goods, transport materials and perform automated tasks.

A robot navigation system needs to calculate and update the positions of objects or movement points when its orientation or movement scale changes.

Matrix algebra can be used to perform these coordinate transformations.

### Assumptions

- The robot operates in a two-dimensional warehouse environment.
- Robot positions are represented using x and y coordinates.
- The robot rotates through 30 degrees.
- A scaling factor of 1.5 is applied to the coordinates.
- The transformation is performed around the coordinate origin.

### Input Data

The robot's original coordinate positions are:

```text
[[2, 1],
 [4, 1],
 [4, 3],
 [2, 3]]
```

### Operations Performed

1. Create a matrix containing the original robot positions.
2. Create a rotation matrix for 30 degrees.
3. Create a scaling matrix with a factor of 1.5.
4. Combine the two matrices using multiplication.
5. Calculate the new robot coordinates.

### Expected Results

The transformed robot positions are approximately:

```text
[[1.8481 2.7990]
 [4.4462 4.2990]
 [2.9462 6.8971]
 [0.3481 5.3971]]
```

### Interpretation

The results show that the original robot coordinates have changed after applying rotation and scaling transformations.

This demonstrates how matrix algebra can support coordinate calculations in robotics and automated warehouse systems.

The transformation is a mathematical illustration; a real robot navigation system would also require physical positioning, obstacle detection and movement controls.

## 11. Conclusion

This task demonstrates how matrix algebra and matrix operations are applied in scientific computing.

The program creates coordinate matrices, performs rotation and scaling transformations, multiplies matrices and calculates a determinant.

It also demonstrates how matrix operations can be applied to robot coordinate transformations.

The exercise improves understanding of matrices and their practical importance in computer graphics, robotics and engineering applications.
