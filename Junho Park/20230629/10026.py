# this is my solution for BaekJoon 10026
# 
# https://www.acmicpc.net/problem/10026
#
# Reference: https://velog.io/@uoayop/BOJ-10026-%EC%A0%81%EB%A1%9D%EC%83%89%EC%95%BD-Python
from sys import stdin
import sys

sys.setrecursionlimit(100000)

def dfs(x, y):
    # left, down, right, up
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    visited[x][y] = True
    now_color = picture[x][y]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N:
            if visited[nx][ny] == False:
                if picture[nx][ny] == now_color:
                    dfs(nx, ny)

# number of rows of a picture
N = int(stdin.readline())

# the picture is N x N
picture = []
for _ in range(N):
    picture.append(list(stdin.readline().strip()))

# N x N matrix to store visit flags
visited = [[False]*N for _ in range(N)]

# to store number of color regions for normal people
col_cnt = 0

# to store number of color regions for people like JaeJun Jeon in The Glory the drama on Netflix
jae_cnt = 0

# run first for normal people
for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            dfs(i, j)
            col_cnt += 1

# run second for people like JaeJun Jeon
for i in range(N):
    for j in range(N):
        if picture[i][j] == 'G':
            picture[i][j] = 'R'
visited = [[False]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            dfs(i, j)
            jae_cnt += 1

print(col_cnt, jae_cnt)