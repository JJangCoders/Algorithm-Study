# this is my solution for BaekJoon 2178
#
# https://www.acmicpc.net/problem/2178
#
# Reference: https://yuna0125.tistory.com/61

from sys import stdin
from collections import deque

def bfs(x, y):
    # left, down, right, up
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if miro[nx][ny] == 1:
                    q.append((nx, ny))
                    miro[nx][ny] = miro[x][y] + 1

N, M = map(int, stdin.readline().split())

miro = []

for _ in range(N):
    miro.append(list(map(int, stdin.readline().strip())))

bfs(0, 0)

print(miro[N-1][M-1])