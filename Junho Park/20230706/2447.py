# this is my solution for BaekJoon 2447
# 별찍기 - 10
# https://www.acmicpc.net/problem/2447

N = int(input())

stars = [['*'] * (N) for _ in range(N)]

def spacing(N, x, y):
    if N == 1:
        return
    for i in range(N//3, 2*(N//3)):
        for j in range(N//3, 2*(N//3)):
            stars[i + x][j + y] = ' '
    spacing(N//3, x, y)                         # left top
    spacing(N//3, N//3+x, y)                    # middle top
    spacing(N//3, 2*(N//3)+x, y)                # right top
    spacing(N//3, x, N//3 + y)                  # left middle
    spacing(N//3, 2*(N//3) + x, N//3 + y)       # center
    spacing(N//3, 2*(N//3) + x, N//3 + y)       # right middle
    spacing(N//3, x, 2*(N//3) + y)              # left bottom
    spacing(N//3, N//3 + x, 2*(N//3) + y)       # middle bottom
    spacing(N//3, 2*(N//3) + x, 2*(N//3) + y)   # right bottom

spacing(N, 0, 0)

for i in range(N):
    for j in range(N):
        print(stars[i][j], end='')
    print()