# This is my solution for BaekJoon 2169
#
# https://www.acmicpc.net/problem/2169
#
# Reference: https://wooono.tistory.com/605

from sys import stdin

N, M = map(int, stdin.readline().split())

terrain = []

for _ in range(N):
    terrain.append(list(map(int, stdin.readline().split())))

for j in range(1, M):
    terrain[0][j] += terrain[0][j-1]

for i in range(1, N):
    fromLeft = terrain[i][:]
    fromRight = terrain[i][:]

    for j in range(M):
        if j == 0:
            fromLeft[j] += terrain[i-1][j]
        else:
            fromLeft[j] += max(terrain[i-1][j], fromLeft[j-1])
    for j in range(M-1, -1, -1):
        if j == M-1:
            fromRight[j] += terrain[i-1][j]
        else:
            fromRight[j] += max(terrain[i-1][j], fromRight[j+1])
    for j in range(M):
        terrain[i][j] = max(fromLeft[j], fromRight[j])

print(terrain[N-1][M-1])