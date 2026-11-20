
# TASK 4: FLOATING-POINT ARITHMETIC AND NUMERICAL ERRORS

## 1. Introduction

Floating-point arithmetic is a method computers use to represent and calculate real numbers.

Computers have limited binary storage precision. As a result, some decimal numbers cannot be represented exactly, which can lead to small numerical errors.

This task examines floating-point representation, absolute error, relative error and numerical stability.

## 2. Problem Statement

A computer program compares the result of 0.1 + 0.2 with 0.3 and unexpectedly reports False.

This happens because computers store some decimal values as approximations using binary floating-point representation.

The program demonstrates this problem and explores how numerical errors can be measured and reduced.

## 3. Objectives

The objectives of this task are:

- To understand floating-point arithmetic.
- To identify numerical errors in computer calculations.
- To calculate absolute and relative errors.
- To understand the difference between round-off and truncation errors.
- To compare numerically unstable and stable mathematical expressions.
- To apply accurate numerical calculations to a real-world financial problem.

## 4. Mathematical Concepts

### A. Floating-point representation

Computers use a finite number of binary digits to represent real numbers.

Some decimal values, such as 0.1 and 0.2, cannot be represented exactly in binary floating-point format.

This may produce small differences during calculations.

### B. Absolute error

Absolute error measures the difference between the true value and the approximate value.

Formula:

Absolute Error = |True Value - Approximate Value|

### C. Relative error

Relative error measures the absolute error in relation to the true value.

Formula:

Relative Error = Absolute Error / |True Value|

To express it as a percentage:

Relative Error (%) = Relative Error × 100

### D. Round-off error

Round-off error occurs when a number is stored or calculated using limited precision.

### E. Truncation error

Truncation error occurs when an exact mathematical process is replaced by an approximation or stopped after a limited number of steps.

## 5. Input Values

The program uses the following values:

- 0.1 and 0.2 for floating-point comparison.
- 0.3 as the expected result.
- Square root of 2 as the true value.
- 1.414 as the approximate value.
- 1e-4, 1e-8 and 1e-12 for numerical stability testing.

For the banking application, the program uses these transaction amounts:

KES 10.10, KES 20.20, KES 30.30, KES 15.40 and KES 24.00.

## 6. Mathematical Operations Performed

The program performs the following operations:

**A. Floating-point addition**

0.1 + 0.2

The result is compared with 0.3 using ordinary equality and NumPy's `np.isclose()` function.

**B. Absolute error**

Absolute Error = |True Value - Approximate Value|

**C. Relative error**

Relative Error = Absolute Error / |True Value|

**D. Numerical stability**

The program compares two mathematically equivalent expressions:

Direct formula:

(√(1 + x) - 1) / x

Stable formula:

1 / (√(1 + x) + 1)

The stable expression reduces cancellation error when x is very small.

**E. Financial calculation**

The program adds transaction amounts using Python's Decimal class to avoid ordinary binary floating-point representation issues in money calculations.

## 7. Python Libraries Used

The program uses:

- **NumPy:** Performs numerical calculations and approximate comparisons.
- **Decimal:** Supports accurate decimal arithmetic for financial calculations.

The libraries are imported using:

`import numpy as np`

`from decimal import Decimal`

## 8. Expected Program Output

```text
PART 1: FLOATING-POINT COMPARISON
---------------------------------
0.1 + 0.2 = 0.30000000000000004
Exact comparison: False
Tolerance-based comparison: True

PART 2: ERROR CALCULATION
-------------------------
True value: 1.41421356
Approximate value: 1.414
Absolute error: 0.00021356
Relative error: 0.01510114%

PART 3: NUMERICAL STABILITY
---------------------------
x=1e-04: direct=0.499987500624, stable=0.499987500625
x=1e-08: direct=0.499999996961, stable=0.499999998750
x=1e-12: direct=0.500044450291, stable=0.500000000000

PART 4: PARAMETER CHANGE
------------------------
New approximate value: 1.4142
New absolute error: 0.00001356
New relative error: 0.00095900%

PART 5: BANKING TRANSACTION ANALYSIS
------------------------------------
Individual transactions: [Decimal('10.10'), Decimal('20.20'), Decimal('30.30'), Decimal('15.40'), Decimal('24.00')]
Total transaction amount: 100.00
Currency: KES
```

## 9. Interpretation of Results

The calculation of 0.1 + 0.2 produces 0.30000000000000004 instead of exactly 0.3.

Therefore, the exact comparison returns False.

However, `np.isclose()` returns True because it checks whether the two values are sufficiently close within a numerical tolerance.

The absolute error of the square root approximation is approximately 0.00021356.

The relative error is approximately 0.01510114%.

The numerical stability test also demonstrates that the direct formula becomes less accurate for very small values of x, while the stable formula gives a result closer to 0.5.

## 10. Changing an Input Parameter

The original approximate value of the square root of 2 is:

1.414

The program is modified to use:

1.4142

The original absolute error is approximately 0.00021356.

After changing the approximate value, the absolute error reduces to approximately 0.00001356.

The relative error also reduces from approximately 0.01510114% to 0.00095900%.

This demonstrates that using a more accurate approximation reduces numerical error.

## 11. Related Real-World Application

### Banking and Financial Transaction System

Financial systems perform calculations involving deposits, withdrawals, payments and account balances.

Even small numerical errors can cause problems when many transactions are processed.

The program is therefore modified to calculate the total value of five financial transactions using Python's Decimal class.

### Assumptions

- All transactions are recorded in Kenyan Shillings (KES).
- All transaction values are provided to two decimal places.
- All five transactions are valid.
- The program calculates their combined total.

### Input Data

| Transaction | Amount |
|---|---:|
| Transaction 1 | KES 10.10 |
| Transaction 2 | KES 20.20 |
| Transaction 3 | KES 30.30 |
| Transaction 4 | KES 15.40 |
| Transaction 5 | KES 24.00 |

### Mathematical Operation

Total Amount = Sum of all transactions

Total = 10.10 + 20.20 + 30.30 + 15.40 + 24.00

### Results

Total transaction amount = KES 100.00

### Interpretation

The program successfully calculates the total value of the five transactions.

Using Decimal helps prevent the unexpected binary floating-point representation differences that can occur when ordinary floating-point numbers are used for financial calculations.

This demonstrates the importance of numerical accuracy in banking and financial applications.

## 12. Conclusion

This task demonstrates how floating-point arithmetic can introduce numerical errors into computer calculations.

It explains absolute error, relative error, round-off error, truncation error and numerical stability.

The program also demonstrates how NumPy can be used for tolerance-based comparisons and how Decimal can support accurate financial calculations.

The exercise improves understanding of numerical accuracy and its importance in scientific computing and real-world applications.
