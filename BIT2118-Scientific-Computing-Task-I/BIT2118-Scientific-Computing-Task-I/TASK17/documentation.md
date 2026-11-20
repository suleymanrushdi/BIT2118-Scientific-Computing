
# TASK 17: ORDINARY DIFFERENTIAL EQUATIONS - EULER METHOD

## 1. Introduction
An ordinary differential equation (ODE) describes how a quantity changes with respect to another variable, such as time.

This task uses Euler's method and Newton's Law of Cooling to predict how the temperature of a hot object decreases over time.

## 2. Input Values
- Initial temperature: 90°C
- Ambient temperature: 25°C
- Cooling constant: 0.12
- Time step: 1 minute
- Total simulation time: 30 minutes

## 3. Mathematical Concept
Newton's Law of Cooling is represented by:

dT/dt = -k(T - T_ambient)

Euler's method uses the following formula:

T_next = T_current + h × cooling_rate

The method estimates the temperature at each new time step.

## 4. Program Implementation
The program uses Python, NumPy and Matplotlib.

NumPy creates the time values and stores the temperature results. Euler's method calculates the temperature at each step. Matplotlib displays the cooling process in a graph.

The program also calculates the exact mathematical solution to compare its accuracy with Euler's method.

## 5. Output Interpretation
The Euler result and exact result show the estimated temperature after 30 minutes.

The difference between the two values represents the numerical error.

The graph shows that the object's temperature decreases gradually towards the surrounding temperature.

## 6. Changing an Input Parameter
The time step is initially 1 minute.

Change h = 1.0 to h = 0.5 and run the program again.

A smaller time step generally improves the accuracy of Euler's method because the calculation uses shorter intervals.

## 7. Real-World Application
This method can be used in food processing, refrigeration systems and industrial temperature monitoring.

For example, a food-processing company can estimate how quickly a hot product cools before packaging or storage.

## 8. Assumptions
- The surrounding temperature remains constant.
- The cooling constant does not change.
- The object cools according to Newton's Law of Cooling.
- The initial temperature is measured accurately.

## 9. Conclusion
This task demonstrates how Euler's method can approximate the solution of an ordinary differential equation.

It shows how numerical methods can predict temperature changes over time and how smaller time steps can improve accuracy.
