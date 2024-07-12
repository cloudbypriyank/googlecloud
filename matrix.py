def transpose_matrix(matrix):
    if not matrix:
        return []

    # Get the number of rows and columns in the matrix
    rows = len(matrix)
    cols = len(matrix[0])

    # Create an empty transposed matrix with dimensions cols x rows
    transposed = [[None] * rows for _ in range(cols)]

    # Fill the transposed matrix
    for r in range(rows):
        for c in range(cols):
            transposed[c][r] = matrix[r][c]

    return transposed

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed_matrix = transpose_matrix(matrix)
print(transposed_matrix)
