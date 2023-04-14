from sys import stdin
from itertools import count

def modulus(a, b):
    return (a % b + b) % b

def slice_and_stretch(matrix, N, M):
    result_list = []
    for i in range(N//2):
        stretched = []
        for j in range(i, M - i):      #left top -> right top
            stretched.append(matrix[i][j])
        if len(stretched) == 0:
            break
        for j in range(i+1, N - i):          #right top -> right bottom
            stretched.append(matrix[j][M-1-i])
        for j in count(M-2-i, -1):    #right bottom -> left bottom
            if j < i:
                break
            stretched.append(matrix[N-1-i][j])
        for j in count(N-2-i, -1):    #left bottom -> left top
            if j < 1 + i:
                break
            stretched.append(matrix[j][i])
        result_list.append(stretched)
    return result_list

def rounding(stretched_lists, R):
    number_of_lists = len(stretched_lists)

    for i in range(number_of_lists):
        n = modulus(R, len(stretched_lists[i]))
        for j in range(n):
            stretched_lists[i].append(stretched_lists[i][0])
            del stretched_lists[i][0]

def list_to_matrix(matrix, stretched_lists, N, M):
    for i in range(len(stretched_lists)):
        for j in range(i, M-i):
            matrix[i][j] = stretched_lists[i][0]
            del stretched_lists[i][0]
        for j in range(i+1, N-i):
            matrix[j][M-1-i] = stretched_lists[i][0]
            del stretched_lists[i][0]
        for j in count(M-2-i, -1):
            if j < i:
                break
            matrix[N-1-i][j] = stretched_lists[i][0]
            del stretched_lists[i][0]
        for j in count(N-2-i, -1):
            if j < 1 + i:
                break
            matrix[j][i] = stretched_lists[i][0]
            del stretched_lists[i][0]
        

N, M, R = map(int, stdin.readline().split())

matrix = []

for i in range(N):
    matrix.append(list(map(int, stdin.readline().split())))

stretched_lists = slice_and_stretch(matrix, N, M)

rounding(stretched_lists, R)

list_to_matrix(matrix, stretched_lists, N, M)

for i in range(N):
    for j in range(M):
        print(matrix[i][j], end = ' ')
    print()