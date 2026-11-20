
# Task 12: Polynomial and Nonlinear Equation Solving

## 1. Introduction
Polynomial and nonlinear equation solving involves finding
unknown values that satisfy mathematical equations.

## 2. Objectives
- Understand polynomial equations.
- Understand nonlinear systems of equations.
- Implement nonlinear equation solving using Python.
- Find the intersection of a circle and a parabola.
- Interpret numerical results.

## 3. Mathematical Concepts

A polynomial equation has the general form:

an*x^n + ... + a1*x + a0 = 0

A nonlinear system contains equations that are not all
linear in their unknown variables.

Numerical methods are used to estimate solutions.

## 4. Real-World Problem

The problem involves finding the intersection points
between a circle and a parabola.

Circle:
x^2 + y^2 = 4

Parabola:
y = x^2 - 1

The objective is to determine the coordinates where
the two curves intersect.

## 5. Inputs
- First initial guess: [1.0, 1.0]
- Second initial guess: [-1.0, 1.0]
- Circle radius: 2
- Circle centre: (0, 0)
- Parabola equation: y = x^2 - 1

## 6. Mathematical Operations
The program defines two nonlinear equations.

It uses scipy.optimize.root to find the intersection
points using different initial guesses.

The residuals measure how close the calculated
solutions are to satisfying both equations.

## 7. Expected Results
The approximate intersection points are:

First intersection:
x = 1.5175
y = 1.3028

Second intersection:
x = -1.5175
y = 1.3028

The residuals should be close to zero.

## 8. Parameter Modification
The program uses two different initial guesses.

Changing the initial guess helps demonstrate how
numerical solvers can locate different solutions
of the same nonlinear system.

## 9. Real-World Applications
- Engineering and mechanical design
- Kinematics
- Chemical equilibrium
- Geometric intersection problems
- Control systems
- Scientific modelling

## 10. Conclusion
The task demonstrates how Python and SciPy can solve
nonlinear systems of equations.

The two initial guesses help identify the two
intersection points between the circle and parabola.
