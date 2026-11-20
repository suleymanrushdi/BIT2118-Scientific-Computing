
# TASK 09: EIGENVALUES AND EIGENVECTORS
# Scientific Computing Assignment

import numpy as np

# Adjacency matrix representing a small computer network.
# Node order: A, B, C, D

A = np.array([
    [0., 1., 1., 0.],
    [1., 0., 1., 1.],
    [1., 1., 0., 1.],
    [0., 1., 1., 0.]
])

# Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

# Identify the dominant eigenvalue
index = np.argmax(np.real(eigenvalues))

dominant_value = np.real(eigenvalues[index])

# Get the corresponding dominant eigenvector
dominant_vector = np.abs(
    np.real(eigenvectors[:, index])
)

# Normalize the eigenvector to obtain importance scores
centrality = dominant_vector / dominant_vector.sum()

nodes = ["A", "B", "C", "D"]

print("TASK 09: EIGENVALUES AND EIGENVECTORS")
print("=" * 50)

print("\nAdjacency Matrix:")
print(A)

print("\nAll Eigenvalues:")
print(np.real(eigenvalues))

print("\nDominant Eigenvalue:")
print(dominant_value)

print("\nEigenvector-Based Network Importance:")

for node, score in zip(nodes, centrality):
    print(f"Node {node}: {score:.4f}")

# Verify the eigenvalue equation Av = lambda*v
v = np.real(eigenvectors[:, index])

print("\nVerification:")
print("A multiplied by v:")
print(A @ v)

print("\nDominant eigenvalue multiplied by v:")
print(dominant_value * v)

print("\nVerification successful:",
      np.allclose(A @ v, dominant_value * v))

print("\nTask 09 completed successfully.")
