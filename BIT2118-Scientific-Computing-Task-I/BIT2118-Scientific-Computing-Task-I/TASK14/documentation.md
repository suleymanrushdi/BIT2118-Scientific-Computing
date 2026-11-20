
# TASK 14: CURVE FITTING AND APPROXIMATION

## 1. Introduction
Curve fitting is a numerical method used to find a mathematical function that best represents a set of observed data.

This task uses Python to model the relationship between the number of concurrent users and server response time.

## 2. Inputs
The program uses the following inputs:

- Concurrent users: 50, 100, 150, 200, 250, 300, 350.
- Response times in milliseconds: 82, 95, 115, 145, 185, 238, 305.
- Prediction target: 400 concurrent users.

## 3. Mathematical Operations
The program uses a quadratic model:

y = ax² + bx + c

The curve_fit() function estimates the parameters a, b and c that best fit the measured data.

The program also calculates Root Mean Square Error (RMSE) to measure the difference between actual and predicted response times.

## 4. Output Interpretation
The program displays:

- The fitted quadratic equation.
- The RMSE value.
- The predicted server response time at 400 concurrent users.

A smaller RMSE indicates that the fitted model is closer to the observed measurements.

The graph displays the original measurements and the fitted quadratic curve.

## 5. Parameter Modification
The prediction target can be changed from 400 users to 450 users.

This produces a new predicted response time because the model evaluates a different number of concurrent users.

## 6. Modified Real-World Application
The program can also be used to estimate the response time of an online banking API under increasing numbers of simultaneous requests.

The input data can be replaced with actual API load-test measurements. The fitted curve can help developers estimate performance and plan server capacity.

## 7. Assumptions
- The measured response times are accurate.
- A quadratic function reasonably represents the observed relationship.
- The server environment remains similar during testing.
- Predictions beyond the measured range are estimates and may be less reliable.

## 8. Conclusion
Curve fitting helps identify relationships between measured variables and make predictions.

This task demonstrates how Python and SciPy can model server performance using a quadratic mathematical function.
