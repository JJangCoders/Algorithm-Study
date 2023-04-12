def circular_rotation(matrix, R):
    n = len(matrix)
    m = len(matrix[0])
    result = [[0] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            ni = (i + R) % n
            nj = (j + R) % m
            result[ni][nj] = matrix[i][j]
    return result


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
R = 1
result = circular_rotation(matrix, R)
print(result)
