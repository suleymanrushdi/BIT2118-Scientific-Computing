
# TASK 3: MATHEMATICAL FUNCTIONS AND VECTORIZATION

## 1. Introduction

Mathematical functions are used in scientific computing to perform calculations on numerical data.

Vectorization is the process of applying mathematical operations to an entire array of values at once instead of processing each value individually using a loop.

Python's NumPy library supports vectorization, making numerical calculations easier and often faster.

## 2. Problem Statement

A network monitoring system collects one million network latency measurements in milliseconds.

The system needs to convert the measurements into seconds and calculate the square of each measurement.

The task compares two approaches:
- Using a normal Python loop.
- Using NumPy vectorization.

The execution times are also compared to understand the performance difference.

## 3. Objectives

The objectives of this task are:

- To understand mathematical functions and vectorization.
- To generate and manipulate numerical data using NumPy.
- To perform mathematical operations on arrays.
- To compare loops and vectorized operations.
- To understand the performance benefits of vectorization.
- To apply vectorization to a related real-world problem.

## 4. Input Values

The program generates 1,000,000 random network latency measurements.

The measurements:
- Have a minimum value of 5 milliseconds.
- Have a maximum value of 250 milliseconds.
- Are generated using NumPy's random number generator.
- Use seed 42 to make the original generated dataset reproducible.

The program also uses machine vibration readings:

2.5, 3.0, 4.2, 1.8 and 5.0 millimetres.

## 5. Mathematical Operations Performed

### A. Conversion of milliseconds to seconds

The conversion formula is:

Seconds = Milliseconds / 1000

### B. Squaring the latency values

Each converted latency value is squared using:

Result = Seconds × Seconds

Mathematically:

y = x²

### C. Vectorized calculation

NumPy performs the conversion and squaring operations on the entire array:

`seconds = latency_ms / 1000.0`

`result = seconds ** 2`

### D. Execution time comparison

The program uses Python's `timeit` module to measure how long the loop and vectorized operations take.

The vectorized operation is timed three times, and its average execution time is calculated.

## 6. Libraries Used

The program uses the following Python libraries:

- **NumPy:** Generates random values and performs numerical operations on arrays.
- **timeit:** Measures the execution time of the two approaches.

The libraries are imported using:

`import numpy as np`

`import timeit`

## 7. Expected Program Output

The first five squared latency values should be approximately:

```text
[0.03787665 0.01266192 0.04637842 0.03092504 0.00078812]
```

The program also displays:

- Number of latency readings: 1,000,000.
- Loop execution time.
- Vectorized execution time.
- Approximate speed-up.
- First five values after changing the maximum latency.
- Machine vibration readings and their converted and squared values.

**Note:** Execution times and speed-up depend on the computer being used. They should be taken from the actual program output rather than assumed.

## 8. Interpretation of Results

The program demonstrates that one million latency measurements can be processed using NumPy vectorization.

The measurements are first converted from milliseconds into seconds and then squared.

The execution time comparison helps demonstrate the performance difference between a normal Python loop and NumPy vectorization.

Vectorization is useful when handling large numerical datasets because it allows mathematical operations to be applied to entire arrays.

## 9. Changing an Input Parameter

The original maximum network latency value is 250 milliseconds.

The program is modified by increasing the maximum latency to 500 milliseconds.

This means the generated dataset can contain larger latency measurements.

After converting and squaring the values, larger latency measurements produce larger squared results.

This demonstrates how changing an input parameter affects the numerical results.

## 10. Related Real-World Application

### Machine Vibration Monitoring System

The original program is modified to analyze machine vibration measurements.

Industrial machines produce vibrations during operation. Monitoring these vibrations can help identify unusual machine behaviour.

The program uses the following vibration readings:

2.5, 3.0, 4.2, 1.8 and 5.0 millimetres.

### Assumptions

- The measurements are collected from a machine during operation.
- All measurements are in millimetres.
- The readings are assumed to be accurate.
- The same conversion and squaring operations are applied to every reading.

### Operations Performed

**Step 1: Convert millimetres into metres**

Metres = Millimetres / 1000

**Step 2: Square the converted readings**

Squared value = Metres × Metres

### Expected Results

Original readings:

```text
[2.5 3.  4.2 1.8 5. ]
```

Converted readings in metres:

```text
[0.0025 0.003  0.0042 0.0018 0.005 ]
```

Squared readings:

```text
[6.25e-06 9.00e-06 1.764e-05 3.24e-06 2.50e-05]
```

### Interpretation

The results show that the vibration measurements can be converted and squared using NumPy vectorization.

The highest original vibration reading is 5.0 millimetres, while the lowest is 1.8 millimetres.

This demonstrates how vectorization can support industrial monitoring and numerical analysis.

The squared values alone do not establish whether a machine is faulty; suitable engineering thresholds and additional analysis would be required.

## 11. Conclusion

This task demonstrates how mathematical functions and vectorization are applied in scientific computing.

The program generates network latency measurements, converts them into seconds, squares the values and compares the execution time of a Python loop with NumPy vectorization.

It also demonstrates how vectorization can be applied to machine vibration monitoring.

The exercise improves understanding of numerical operations, array processing and the importance of efficient computation when working with large datasets.
