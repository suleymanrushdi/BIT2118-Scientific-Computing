
import numpy as np

# ==========================================
# TASK 2: NUMPY ARRAYS AND NUMERICAL COMPUTATION
# ==========================================

# PART 1: Weather Station Temperature Analysis

# 24 hourly temperature readings in degrees Celsius
temperatures_c = np.array([
    18.5, 18.0, 17.8, 17.5, 17.9, 19.0,
    21.5, 23.8, 25.6, 27.1, 28.3, 29.0,
    29.4, 29.1, 28.5, 27.6, 26.2, 24.8,
    23.4, 22.1, 21.0, 20.2, 19.6, 19.0
])

# Perform numerical calculations
mean_temp = np.mean(temperatures_c)
min_temp = np.min(temperatures_c)
max_temp = np.max(temperatures_c)

# Convert Celsius readings to Fahrenheit
temperatures_f = 1.8 * temperatures_c + 32

# Display results
print("PART 1: WEATHER STATION ANALYSIS")
print("--------------------------------")
print(f"Daily mean temperature: {mean_temp:.2f} C")
print(f"Minimum temperature: {min_temp:.2f} C")
print(f"Maximum temperature: {max_temp:.2f} C")
print("First six Fahrenheit readings:", temperatures_f[:6])


# PART 2: PARAMETER CHANGE

# Change the first temperature reading from 18.5 to 25.0
changed_temperatures = temperatures_c.copy()
changed_temperatures[0] = 25.0

changed_mean = np.mean(changed_temperatures)

print("\nPART 2: PARAMETER CHANGE")
print("------------------------")
print(f"New mean temperature: {changed_mean:.2f} C")


# PART 3: RELATED REAL-WORLD APPLICATION
# Electricity consumption monitoring

electricity_kwh = np.array([
    12, 15, 10, 8, 9, 14,
    20, 25, 30, 35, 40, 38
])

# Calculate electricity consumption statistics
mean_usage = np.mean(electricity_kwh)
minimum_usage = np.min(electricity_kwh)
maximum_usage = np.max(electricity_kwh)

# Convert kilowatt-hours to watt-hours
electricity_wh = electricity_kwh * 1000

print("\nPART 3: ELECTRICITY CONSUMPTION ANALYSIS")
print("----------------------------------------")
print(f"Average consumption: {mean_usage:.2f} kWh")
print(f"Minimum consumption: {minimum_usage:.2f} kWh")
print(f"Maximum consumption: {maximum_usage:.2f} kWh")
print("First six readings in Wh:", electricity_wh[:6])
