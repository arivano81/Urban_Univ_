def get_matrix(n, m, value):
    row = []
    matrix = []
    for i in range(n):
        for j in range(m):
            row.append(value)
        matrix.append(row)
        row = []
    return matrix
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)