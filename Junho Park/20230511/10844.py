# This is my solution for BaekJoon 10844
#
# https://www.acmicpc.net/problem/10844

# Reference: https://cotak.tistory.com/12

# First attempt: Timeout
# 
# def stepNumCounter(number, depth):
#     if depth == N:
#         return 1
#     if number == 9:
#         return stepNumCounter(8, depth + 1)
#     elif number == 0:
#         return stepNumCounter(1, depth + 1)
#     else:
#         return stepNumCounter(number - 1, depth + 1) + stepNumCounter(number + 1, depth + 1)

N = int(input())

# caseTable[length][num_before] = number of cases
caseTable = [[0]*10 for _ in range(N+1)]
for i in range(1, 10):
    caseTable[1][i] = 1

for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            caseTable[i][j] = caseTable[i-1][1]
        elif j == 9:
            caseTable[i][j] = caseTable[i-1][8]
        else:
            caseTable[i][j] = caseTable[i-1][j-1] + caseTable[i-1][j+1]

print(sum(caseTable[N]) % 1000000000)