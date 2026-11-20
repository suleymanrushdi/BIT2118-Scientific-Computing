
# TASK 2: NUMPY ARRAYS AND NUMERICAL COMPUTATION

## 1. Introduction

NumPy is a Python library used for numerical computation. It provides support for working with arrays and matrices and performing mathematical operations efficiently.

An array is a collection of values stored in an organized structure. NumPy allows calculations to be performed on entire arrays without writing separate operations for every element.

## 2. Problem Statement

A weather station records temperature readings every hour for 24 hours. The station needs to analyze the collected data by calculating the average, minimum and maximum temperatures.

It also needs to convert the recorded temperatures from degrees Celsius to degrees Fahrenheit.

## 3. Objectives

The objectives of this task are:

- To understand NumPy arrays.
- To create and manipulate numerical arrays.
- To calculate the mean, minimum and maximum values.
- To perform mathematical operations on arrays.
- To understand how NumPy supports scientific computing.

## 4. Input Values

The program uses 24 hourly temperature readings measured in degrees Celsius:

18.5, 18.0, 17.8, 17.5, 17.9, 19.0, 21.5, 23.8, 25.6, 27.1, 28.3, 29.0, 29.4, 29.1, 28.5, 27.6, 26.2, 24.8, 23.4, 22.1, 21.0, 20.2, 19.6 and 19.0.

## 5. Mathematical Operations Performed

The program performs the following operations:

**a) Mean calculation**

The average temperature is calculated using:

Mean = Sum of all temperatures / Number of readings

**b) Minimum temperature**

The program identifies the lowest temperature using NumPy's `np.min()` function.

**c) Maximum temperature**

The program identifies the highest temperature using NumPy's `np.max()` function.

**d) Celsius to Fahrenheit conversion**

The conversion formula is:

F = (1.8 × C) + 32

Where:
- F represents temperature in Fahrenheit.
- C represents temperature in Celsius.

## 6. Python Libraries Used

The program uses NumPy.

The library is imported using:

`import numpy as np`

The following NumPy functions are used:

- `np.array()` – creates a numerical array.
- `np.mean()` – calculates the average.
- `np.min()` – identifies the smallest value.
- `np.max()` – identifies the largest value.

## 7. Expected Program Output

```text
PART 1: WEATHER STATION ANALYSIS
--------------------------------
Daily mean temperature: 23.12 C
Minimum temperature: 17.50 C
Maximum temperature: 29.40 C
First six Fahrenheit readings: [65.3  64.4  64.04 63.5  64.22 66.2 ]

PART 2: PARAMETER CHANGE
------------------------
New mean temperature: 23.39 C

PART 3: ELECTRICITY CONSUMPTION ANALYSIS
----------------------------------------
Average consumption: 21.33 kWh
Minimum consumption: 8.00 kWh
Maximum consumption: 40.00 kWh
First six readings in Wh: [12000 15000 10000  8000  9000 14000]
```

## 8. Interpretation of Results

The average daily temperature is 23.12 degrees Celsius. The lowest recorded temperature is 17.50 degrees Celsius, while the highest is 29.40 degrees Celsius.

The Celsius-to-Fahrenheit conversion demonstrates how NumPy performs mathematical operations on all elements of an array.

The results show that NumPy makes numerical calculations easier and more efficient.

## 9. Changing an Input Parameter

The original first temperature reading was 18.5 degrees Celsius.

The program was modified by changing this value to 25.0 degrees Celsius.

After changing the input, the average temperature increased from 23.12 degrees Celsius to 23.39 degrees Celsius.

This demonstrates that changing an input value affects the final numerical result.

## 10. Related Real-World Application

### Electricity Consumption Monitoring System

The original weather station program was modified to analyze electricity consumption.

A household or organization can use this system to monitor electricity consumption over 12 recorded periods.

The input values are electricity consumption readings measured in kilowatt-hours (kWh):

12, 15, 10, 8, 9, 14, 20, 25, 30, 35, 40 and 38.

### Assumptions

- The readings represent 12 consecutive monitoring periods.
- All readings are measured in kilowatt-hours.
- The readings are assumed to be accurate.

### Operations Performed

The program calculates:
- Average electricity consumption.
- Minimum electricity consumption.
- Maximum electricity consumption.
- Conversion from kilowatt-hours to watt-hours.

The conversion formula is:

Wh = kWh × 1000

### Results

- Average consumption: 21.33 kWh.
- Minimum consumption: 8 kWh.
- Maximum consumption: 40 kWh.
- First six converted readings: 12000, 15000, 10000, 8000, 9000 and 14000 Wh.

### Interpretation

The results help households and organizations understand their electricity consumption patterns.

The average indicates typical consumption across the recorded periods, while the maximum identifies the period with the highest usage.

This application demonstrates how NumPy can be used in real-world energy monitoring systems.

## 11. Conclusion

This task demonstrates how NumPy arrays can be used for numerical computation and mathematical operations.

The program successfully calculates temperature statistics, converts temperatures between units and analyzes electricity consumption.

The exercise has improved my understanding of arrays, numerical operations and the application of scientific computing to real-world problems.
