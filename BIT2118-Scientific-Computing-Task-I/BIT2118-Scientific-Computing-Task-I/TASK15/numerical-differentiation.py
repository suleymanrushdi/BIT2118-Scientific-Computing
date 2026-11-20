
import numpy as np
import matplotlib.pyplot as plt

# GPS samples: time in seconds and position in metres
time = np.array([0, 1, 2, 3, 4, 5, 6], dtype=float)

position = np.array([
    0.0, 4.8, 10.2, 16.1, 22.7, 30.0, 38.0
])

# Create an array to store estimated speeds
speed = np.zeros_like(position)

# Forward difference at the beginning
speed[0] = (
    position[1] - position[0]
) / (
    time[1] - time[0]
)

# Central differences for interior points
for i in range(1, len(time) - 1):
    speed[i] = (
        position[i + 1] - position[i - 1]
    ) / (
        time[i + 1] - time[i - 1]
    )

# Backward difference at the end
speed[-1] = (
    position[-1] - position[-2]
) / (
    time[-1] - time[-2]
)

# Display estimated speeds
print("TASK 15: NUMERICAL DIFFERENTIATION")
print()

for t, x, v in zip(time, position, speed):
    print(
        f"t={t:.0f}s, position={x:.1f}m, "
        f"estimated speed={v:.2f}m/s"
    )

# Plot estimated speed
plt.plot(time, speed, marker="o")
plt.xlabel("Time (seconds)")
plt.ylabel("Estimated speed (m/s)")
plt.title("Speed Estimated from GPS Position Data")
plt.grid(True)
plt.show()
