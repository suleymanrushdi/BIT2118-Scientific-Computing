
# TASK 09: EIGENVALUES AND EIGENVECTORS

## 1. Introduction

Eigenvalues and eigenvectors are important concepts in linear algebra and scientific computing.

An eigenvector is a non-zero vector whose direction remains unchanged when a matrix transformation is applied. The eigenvalue represents the scaling factor associated with that vector.

The mathematical relationship is:

Av = λv

Where:
- A is a square matrix.
- v is an eigenvector.
- λ is the corresponding eigenvalue.

## 2. Problem Statement

Computer networks contain interconnected nodes that communicate with one another.

Identifying the most influential nodes can help administrators understand network structure and importance.

This task uses eigenvalues and eigenvectors to calculate the relative importance of nodes in a small computer network.

## 3. Objectives

- Understand eigenvalues and eigenvectors.
- Calculate eigenvalues using NumPy.
- Calculate corresponding eigenvectors.
- Identify the dominant eigenvalue.
- Determine eigenvector-based network importance scores.
- Verify the eigenvalue equation.

## 4. Input Data

The program uses an adjacency matrix representing four network nodes:

A = [[0, 1, 1, 0],
     [1, 0, 1, 1],
     [1, 1, 0, 1],
     [0, 1, 1, 0]]

The nodes are labelled A, B, C and D.

A value of 1 indicates a connection between two nodes, while 0 indicates no direct connection.

## 5. Mathematical Operations

The program performs the following operations:

1. Creates the adjacency matrix.
2. Calculates eigenvalues and eigenvectors using NumPy.
3. Identifies the largest eigenvalue.
4. Extracts its corresponding eigenvector.
5. Normalizes the eigenvector to obtain importance scores.
6. Verifies the relationship Av = λv.

## 6. Expected Results

The dominant eigenvalue is approximately:

2.5616

The normalized eigenvector-based importance scores are:

Node A: 0.2192
Node B: 0.2808
Node C: 0.2808
Node D: 0.2192

Nodes B and C have the highest importance scores in this example.

## 7. Changing Input Data

The adjacency matrix can be modified to represent a different network structure.

For example, adding a connection between nodes A and D requires changing the corresponding matrix entries from 0 to 1.

The program will recalculate the eigenvalues, eigenvectors and importance scores based on the new network.

## 8. Real-World Applications

Eigenvalues and eigenvectors are applied in:

- Computer network analysis.
- Google's PageRank concepts.
- Structural vibration analysis.
- Principal Component Analysis (PCA).
- Image compression.
- Stability analysis of dynamic systems.
- Scientific simulations.

## 9. Assumptions and Limitations

- The input must be a square matrix.
- The network is represented as an undirected graph.
- The matrix is assumed to contain numerical connection values.
- The dominant eigenvector is used to estimate node importance.
- Eigenvector-based importance does not necessarily represent every aspect of network influence.

## 10. Interpretation

The results show that nodes B and C have higher eigenvector-based importance scores than nodes A and D.

This happens because B and C have stronger positions in the network connection structure.

The verification confirms that the calculated eigenvector satisfies the eigenvalue equation within numerical precision.

## 11. Conclusion

The task successfully demonstrates how eigenvalues and eigenvectors can be calculated using Python and NumPy.

It also shows how eigenvector-based importance can help analyse the structure of a computer network.
