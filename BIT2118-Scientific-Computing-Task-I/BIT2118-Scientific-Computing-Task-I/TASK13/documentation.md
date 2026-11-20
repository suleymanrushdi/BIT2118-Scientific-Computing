
# TASK 13: INTERPOLATION

## 1. Introduction
Interpolation is a numerical method used to estimate unknown values between known data points.

This task uses Python to estimate temperature readings between hourly measurements using linear interpolation and cubic spline interpolation.

## 2. Inputs
The program uses the following hourly temperature measurements:

- Hours: 8, 9, 10, 11, 12, 13, 14
- Temperatures: 18.0, 20.0, 22.5, 24.0, 25.0, 25.5, 25.0 degrees Celsius.

The target time is 10:30 AM.

## 3. Mathematical Operations
The program applies two interpolation methods:

- Linear interpolation estimates values using a straight line between two known points.
- Cubic spline interpolation uses smooth cubic polynomial curves between data points.

## 4. Output Interpretation
The program estimates the temperature at 10:30 AM using both methods.

It also generates a graph showing the original hourly measurements and the estimated temperatures.

The graph helps compare the linear and cubic spline interpolation methods.

## 5. Parameter Modification
The target time can be changed from 10.5 to 11.5 to estimate the temperature at 11:30 AM.

Changing the target time produces a different estimated temperature because the program evaluates a different point in the dataset.

## 6. Real-World Application
Interpolation can be used in weather monitoring systems to estimate temperatures between sensor readings.

For example, a weather station that records temperature every hour can use interpolation to estimate temperatures every ten minutes.

## 7. Assumptions
- The recorded hourly temperatures are accurate.
- Temperature changes smoothly between measurements.
- The given data is sufficient to estimate intermediate values.

## 8. Conclusion
The task demonstrates how linear and cubic spline interpolation can estimate unknown values between known measurements.

Both methods are useful in scientific computing, engineering and data analysis.
