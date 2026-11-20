
# Task 11: Newton-Raphson and Secant Methods

## 1. Introduction
Newton-Raphson and Secant are numerical methods used to
find approximate solutions to nonlinear equations.

## 2. Objectives
- Understand the Newton-Raphson method.
- Understand the Secant method.
- Implement both methods using Python.
- Compare their results.
- Apply numerical methods to financial calculations.

## 3. Mathematical Concepts

### Newton-Raphson Method
The method uses the formula:

x(n+1) = x(n) - f(x(n))/f'(x(n))

It uses the derivative of a function to improve an
initial estimate of the root.

### Secant Method
The Secant method estimates the derivative using two
previous values.

It does not require an explicitly calculated derivative.

## 4. Real-World Problem

A financial application needs to calculate the
Internal Rate of Return (IRR) of an investment.

The initial investment is 10,000, followed by annual
cash inflows of 3,000, 3,500, 4,000 and 2,500.

The objective is to find the interest rate at which
the Net Present Value (NPV) becomes zero.

## 5. Inputs
- Initial investment: -10,000
- First annual cash inflow: 3,000
- Second annual cash inflow: 3,500
- Third annual cash inflow: 4,000
- Fourth annual cash inflow: 2,500
- Newton initial guess: 0.10
- Secant initial guesses: 0.05 and 0.20
- Tolerance: 1e-12

## 6. Operations and Algorithms
The program defines the NPV function and its derivative.

It then applies:
1. Newton-Raphson using the derivative.
2. Secant using two initial estimates.

Both methods calculate the approximate IRR.

## 7. Expected Results
Both methods should produce an IRR of approximately
11.542461%.

The NPV at the calculated rate should be approximately zero.

## 8. Real-World Applications
- Investment analysis
- Financial planning
- Circuit calculations
- Engineering models
- Nonlinear equation solving

## 9. Assumptions
- Cash flows occur at the end of each year.
- The initial investment occurs at year zero.
- The interest rate is greater than -100%.
- The selected initial guesses allow convergence.

## 10. Conclusion
Newton-Raphson and Secant methods successfully estimate
the Internal Rate of Return of an investment.

The results demonstrate how numerical methods can
support financial decision-making.
