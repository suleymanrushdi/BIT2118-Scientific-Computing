
import numpy as np
from decimal import Decimal

# ==========================================
# TASK 4: FLOATING-POINT ARITHMETIC
# AND NUMERICAL ERRORS
# ==========================================

# PART 1: Floating-point comparison

calculated = 0.1 + 0.2
expected = 0.3

print("PART 1: FLOATING-POINT COMPARISON")
print("---------------------------------")
print("0.1 + 0.2 =", calculated)
print("Exact comparison:", calculated == expected)
print("Tolerance-based comparison:", np.isclose(calculated, expected))


# PART 2: Absolute and relative error

true_value = np.sqrt(2)
approx_value = 1.414

absolute_error = abs(true_value - approx_value)
relative_error = absolute_error / abs(true_value)

print("\nPART 2: ERROR CALCULATION")
print("-------------------------")
print(f"True value: {true_value:.8f}")
print(f"Approximate value: {approx_value:.3f}")
print(f"Absolute error: {absolute_error:.8f}")
print(f"Relative error: {relative_error:.8%}")


# PART 3: Numerically unstable versus stable formula

print("\nPART 3: NUMERICAL STABILITY")
print("---------------------------")

for x in [1e-4, 1e-8, 1e-12]:
    direct = (np.sqrt(1 + x) - 1) / x
    stable = 1 / (np.sqrt(1 + x) + 1)

    print(
        f"x={x:.0e}: "
        f"direct={direct:.12f}, "
        f"stable={stable:.12f}"
    )


# PART 4: CHANGE AN INPUT PARAMETER

# Improve the approximate value of square root of 2
changed_approx_value = 1.4142

changed_absolute_error = abs(true_value - changed_approx_value)
changed_relative_error = changed_absolute_error / abs(true_value)

print("\nPART 4: PARAMETER CHANGE")
print("------------------------")
print("New approximate value:", changed_approx_value)
print(f"New absolute error: {changed_absolute_error:.8f}")
print(f"New relative error: {changed_relative_error:.8%}")


# PART 5: RELATED REAL-WORLD APPLICATION
# Banking and financial calculations

# Decimal is used to represent money accurately
transactions = [
    Decimal("10.10"),
    Decimal("20.20"),
    Decimal("30.30"),
    Decimal("15.40"),
    Decimal("24.00")
]

total_balance = sum(transactions)

print("\nPART 5: BANKING TRANSACTION ANALYSIS")
print("------------------------------------")
print("Individual transactions:", transactions)
print("Total transaction amount:", total_balance)
print("Currency: KES")
