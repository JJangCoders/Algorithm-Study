import sys
from collections import deque

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

width, height = map(int, sys.stdin.readline().split())

# 토마토 상자의 정보를 저장하기 위한 bracket 선언
bracket = [list(map(int, sys.stdin.readline().split())) for _ in range(height)]

# 익은 토마토의 좌표를 저장하기 위한 ripe_tomatoes 선언
ripe_tomatoes = deque()

# 최초 익은 토마토의 좌표를 ripe_tomatoes에 저장
for y in range(height):
    for x in range(width):
        if bracket[y][x] == 1:
            ripe_tomatoes.append((y, x))

day = -1

# ripe_tomatoes를 기준으로 탐색
while ripe_tomatoes:
    for _ in range(len(ripe_tomatoes)):
        current_y, current_x = ripe_tomatoes.popleft()
        for move_y, move_x in directions:
            next_x, next_y = current_x + move_x, current_y + move_y
            if 0 <= next_x < width and 0 <= next_y < height and bracket[next_y][next_x] == 0:
                bracket[next_y][next_x] = bracket[current_y][current_x] + 1
                ripe_tomatoes.append((next_y, next_x))
    day += 1

# bracket에 0이 존재하는 경우 => 모든 토마토가 익지 못하는 상황
for row in bracket:
    if 0 in row:
        print(-1)
        exit(0)

print(day)
