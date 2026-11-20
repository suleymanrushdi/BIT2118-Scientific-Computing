
# TASK 16: NUMERICAL INTEGRATION

## 1. Introduction
Numerical integration is a mathematical technique used to estimate the total area under a curve when an exact mathematical solution is difficult to obtain.

In this task, numerical integration is used to estimate electrical energy consumption from smart-meter power readings.

## 2. Input Data
The program uses power readings collected every two hours.

Time in hours: 0, 2, 4, 6, 8, 10, 12.

Power in kilowatts: 0.8, 1.0, 1.4, 1.8, 1.6, 1.2, 0.9.

## 3. Numerical Methods Used

### Trapezoidal Rule
The trapezoidal rule estimates the area under a curve by dividing it into trapezoids and calculating their combined area.

### Simpson's Rule
Simpson's rule estimates the area under a curve using parabolic segments. It can provide a more accurate estimate for smoothly changing data.

## 4. Program Implementation
Python and the NumPy and SciPy libraries were used.

The program calculates electrical energy using both methods and compares their results.

## 5. Output Interpretation
The output gives two estimates of energy consumption in kilowatt-hours (kWh).

The difference shows how much the two numerical methods vary when applied to the same readings.

## 6. Changing an Input Parameter
The power reading at hour 6 was originally 1.8 kW.

Change it to 2.0 kW and run the program again.

The estimated energy consumption will increase because the recorded power at that time is higher.

## 7. Real-World Application
A smart electricity meter can record power consumption at regular intervals.

An electricity company can use numerical integration to estimate the total energy consumed by a household or business. This information can support electricity billing and energy monitoring.

## 8. Assumptions
- Power readings are recorded accurately.
- Readings are taken at regular two-hour intervals.
- Power consumption changes between readings.
- The numerical methods provide estimates of total energy consumption.

## 9. Conclusion
This task demonstrates how numerical integration can estimate total electrical energy consumption.

The trapezoidal and Simpson's rules provide two approaches for estimating energy from smart-meter readings.
