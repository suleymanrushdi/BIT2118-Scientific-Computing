
# TASK 18: NUMERICAL SOLUTION OF ODEs USING SCIPY

## 1. Introduction
An ordinary differential equation describes how a quantity changes over time.

This task uses SciPy's solve_ivp() function to simulate the charging of a capacitor in an RC electrical circuit.

## 2. Input Values
- Supply voltage: 5 volts
- Resistance: 1000 ohms
- Capacitance: 0.001 farads
- Initial capacitor voltage: 0 volts
- Simulation time: 5 seconds

## 3. Mathematical Concept
The RC charging equation is:

dV/dt = (Vs - V)/(R*C)

Where:
- V is the capacitor voltage.
- Vs is the supply voltage.
- R is the resistance.
- C is the capacitance.

The solve_ivp() function numerically solves this differential equation over the specified time interval.

## 4. Program Implementation
The program uses Python, NumPy, SciPy and Matplotlib.

NumPy generates the time values. SciPy solves the differential equation using solve_ivp(). Matplotlib displays the numerical and exact solutions.

## 5. Output Interpretation
The solver success message confirms whether the numerical solver completed successfully.

The capacitor voltage after five seconds should be approximately 4.9663 volts.

The maximum error compares the numerical result with the exact mathematical solution.

The graph shows the capacitor voltage increasing towards the supply voltage of 5 volts.

## 6. Changing an Input Parameter
Change the supply voltage from 5.0 volts to 6.0 volts.

Run the program again.

The final capacitor voltage will increase because the capacitor is charging towards a higher supply voltage.

## 7. Real-World Application
This method can be used in electronic circuit simulation, battery systems and electrical engineering.

For example, an engineer can use numerical differential equation solvers to predict how quickly a capacitor charges in an electronic device.

## 8. Assumptions
- Resistance remains constant.
- Capacitance remains constant.
- The supply voltage is constant.
- The capacitor starts with zero voltage.
- The circuit follows the standard RC charging model.

## 9. Conclusion
This task demonstrates how SciPy can solve ordinary differential equations numerically.

The results show how capacitor voltage changes over time and how numerical solutions can be compared with exact mathematical solutions.
