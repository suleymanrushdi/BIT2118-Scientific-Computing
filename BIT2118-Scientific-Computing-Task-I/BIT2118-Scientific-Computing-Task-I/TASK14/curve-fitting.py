
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Number of concurrent users and measured server response time
users = np.array([50, 100, 150, 200, 250, 300, 350], dtype=float)

response_ms = np.array([
    82, 95, 115, 145, 185, 238, 305
], dtype=float)

# Quadratic mathematical model
def model(x, a, b, c):
    return a*x**2 + b*x + c

# Fit the curve to the measured data
parameters, covariance = curve_fit(
    model, users, response_ms
)

a, b, c = parameters

# Calculate predicted values
predicted = model(users, a, b, c)

# Calculate Root Mean Square Error
rmse = np.sqrt(np.mean((response_ms - predicted)**2))

# Display results
print("TASK 14: CURVE FITTING AND APPROXIMATION")

print(
    f"Fitted model: y = {a:.6f}x^2 + "
    f"{b:.4f}x + {c:.2f}"
)

print(f"RMSE: {rmse:.2f} ms")

print(
    f"Predicted response at 400 users: "
    f"{model(400, a, b, c):.2f} ms"
)

# Generate points for the fitted curve
x_plot = np.linspace(users.min(), 400, 300)

# Plot measured data and fitted curve
plt.scatter(
    users,
    response_ms,
    label="Measurements"
)

plt.plot(
    x_plot,
    model(x_plot, a, b, c),
    label="Fitted curve"
)

plt.xlabel("Concurrent users")
plt.ylabel("Response time (ms)")
plt.title("Server Response-Time Curve Fitting")
plt.legend()
plt.grid(True)
plt.show()
