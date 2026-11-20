
import numpy as np

# ==========================================
# TASK 5: MATRIX ALGEBRA AND MATRIX OPERATIONS
# ==========================================

# PART 1: Original coordinates of a square
# Each row represents one point [x, y]

points = np.array([
    [0.0, 0.0],
    [1.0, 0.0],
    [1.0, 1.0],
    [0.0, 1.0]
])

# Rotation angle in degrees
angle = np.deg2rad(45)

# Create rotation matrix
rotation = np.array([
    [np.cos(angle), -np.sin(angle)],
    [np.sin(angle), np.cos(angle)]
])

# Create scaling matrix
scale = np.array([
    [2.0, 0.0],
    [0.0, 1.5]
])

# Combine rotation and scaling matrices
transformation = rotation @ scale

# Transform the original coordinates
transformed_points = points @ transformation.T

print("PART 1: ORIGINAL MATRIX TRANSFORMATION")
print("--------------------------------------")
print("Original points:")
print(points)

print("\nTransformation matrix:")
print(transformation)

print("\nTransformed points:")
print(np.round(transformed_points, 4))

# Calculate determinant
determinant = np.linalg.det(transformation)

print("\nDeterminant:", round(determinant, 4))


# PART 2: CHANGE AN INPUT PARAMETER
# Change rotation angle from 45 degrees to 90 degrees

changed_angle = np.deg2rad(90)

changed_rotation = np.array([
    [np.cos(changed_angle), -np.sin(changed_angle)],
    [np.sin(changed_angle), np.cos(changed_angle)]
])

changed_transformation = changed_rotation @ scale

changed_points = points @ changed_transformation.T

print("\nPART 2: PARAMETER CHANGE")
print("------------------------")
print("New rotation angle: 90 degrees")
print("New transformed points:")
print(np.round(changed_points, 4))


# PART 3: RELATED REAL-WORLD APPLICATION
# Robot movement in a warehouse

robot_positions = np.array([
    [2.0, 1.0],
    [4.0, 1.0],
    [4.0, 3.0],
    [2.0, 3.0]
])

# Robot rotates by 30 degrees
robot_angle = np.deg2rad(30)

robot_rotation = np.array([
    [np.cos(robot_angle), -np.sin(robot_angle)],
    [np.sin(robot_angle), np.cos(robot_angle)]
])

# Apply a scaling factor of 1.5
robot_scale = np.array([
    [1.5, 0.0],
    [0.0, 1.5]
])

robot_transformation = robot_rotation @ robot_scale

# Transform robot positions
new_robot_positions = robot_positions @ robot_transformation.T

print("\nPART 3: ROBOT POSITION TRANSFORMATION")
print("-------------------------------------")
print("Original robot positions:")
print(robot_positions)

print("\nNew robot positions:")
print(np.round(new_robot_positions, 4))
