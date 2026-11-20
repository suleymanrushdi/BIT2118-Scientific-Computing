
# TASK 15: NUMERICAL DIFFERENTIATION

## 1. Introduction
Numerical differentiation is a mathematical method used to estimate the derivative of a function using numerical data.

A derivative measures the rate at which a quantity changes.

This task estimates the speed of a moving vehicle using GPS position measurements.

## 2. Inputs
The program uses:

- Time measurements: 0, 1, 2, 3, 4, 5 and 6 seconds.
- Position measurements: 0.0, 4.8, 10.2, 16.1, 22.7, 30.0 and 38.0 metres.

## 3. Mathematical Operations
The program uses three numerical differentiation methods:

- Forward difference: estimates the derivative at the first data point.
- Central difference: estimates derivatives at interior data points.
- Backward difference: estimates the derivative at the last data point.

Speed is calculated as the rate of change of position with respect to time.

## 4. Output Interpretation
The program displays the time, vehicle position and estimated speed at each measurement.

The graph shows how the estimated speed changes over time.

An increasing speed indicates that the vehicle is moving faster.

## 5. Parameter Modification
Change the position measurement at 6 seconds from 38.0 metres to 42.0 metres.

Run the program again and observe how the estimated speed at the final measurement changes.

This demonstrates how changing input measurements affects numerical differentiation.

## 6. Modified Real-World Application
The program can be adapted for monitoring the speed of delivery vehicles using GPS tracking data.

A transport company can use the estimated speeds to monitor vehicle movement and identify unusual changes in speed.

## 7. Assumptions
- GPS position measurements are reasonably accurate.
- Time measurements are recorded in seconds.
- Position is measured in metres.
- The vehicle moves continuously between measurements.

## 8. Conclusion
Numerical differentiation provides a practical way to estimate rates of change from measured data.

This task demonstrates how GPS position data can be used to estimate vehicle speed using Python.
