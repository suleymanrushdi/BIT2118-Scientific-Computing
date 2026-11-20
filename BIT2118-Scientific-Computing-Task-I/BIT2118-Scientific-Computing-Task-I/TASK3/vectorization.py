
import numpy as np
import timeit

# ==========================================
# TASK 3: MATHEMATICAL FUNCTIONS AND VECTORIZATION
# ==========================================

# PART 1: Generate network latency readings

# Generate 1 million random latency values in milliseconds
rng = np.random.default_rng(42)
latency_ms = rng.uniform(5, 250, 1_000_000)


# PART 2: Using a normal Python loop
def loop_version():
    squared = []

    for value in latency_ms:
        seconds = value / 1000.0
        squared.append(seconds ** 2)

    return squared


# PART 3: Using NumPy vectorization
def vectorized_version():
    seconds = latency_ms / 1000.0
    return seconds ** 2


# Measure execution time
loop_time = timeit.timeit(loop_version, number=1)
vector_time = timeit.timeit(vectorized_version, number=3) / 3

# Calculate the vectorized result
result = vectorized_version()

# Display results
print("TASK 3: MATHEMATICAL FUNCTIONS AND VECTORIZATION")
print("------------------------------------------------")
print("Number of latency readings:", len(latency_ms))
print("First five squared latency values:", result[:5])

print("\nEXECUTION TIME COMPARISON")
print("-------------------------")
print(f"Loop execution time: {loop_time:.4f} seconds")
print(f"Vectorized execution time: {vector_time:.4f} seconds")

if vector_time > 0:
    print(f"Approximate speed-up: {loop_time / vector_time:.1f} times")


# PART 4: CHANGE AN INPUT PARAMETER

# Increase the maximum latency from 250 ms to 500 ms
changed_latency_ms = rng.uniform(5, 500, 1_000_000)

changed_seconds = changed_latency_ms / 1000.0
changed_result = changed_seconds ** 2

print("\nPART 4: PARAMETER CHANGE")
print("------------------------")
print("First five values after changing the maximum latency:")
print(changed_result[:5])


# PART 5: RELATED REAL-WORLD APPLICATION
# Machine vibration measurement

vibration_mm = np.array([2.5, 3.0, 4.2, 1.8, 5.0])

# Convert millimetres to metres
vibration_m = vibration_mm / 1000

# Square each converted reading
squared_vibration = vibration_m ** 2

print("\nPART 5: MACHINE VIBRATION ANALYSIS")
print("----------------------------------")
print("Original readings (mm):", vibration_mm)
print("Converted readings (m):", vibration_m)
print("Squared readings:", squared_vibration)
