import numpy as np

def create_matrix(rows, cols):
    print(f"Enter {rows}x{cols} matrix row by row (space separated):")
    matrix = []
    for i in range(rows):
        while True:
            try:
                row = list(map(float, input(f"Row {i+1}: ").strip().split()))
                if len(row) != cols:
                    print(f"Error: Expected {cols} elements, got {len(row)}.")
                    continue
                matrix.append(row)
                break
            except ValueError:
                print("Invalid input. Please enter numbers.")
    return np.array(matrix)

def add_matrices(m1, m2):
    return np.add(m1, m2)

def subtract_matrices(m1, m2):
    return np.subtract(m1, m2)

def multiply_matrices(m1, m2):
    return np.dot(m1, m2)

def transpose_matrix(m):
    return np.transpose(m)

def determinant_matrix(m):
    if m.shape[0] != m.shape[1]:
        raise ValueError("Determinant only defined for square matrices.")
    return np.linalg.det(m)
