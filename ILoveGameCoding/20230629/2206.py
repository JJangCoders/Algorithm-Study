import sys
from collections import deque

# 이동 방향에 따른 좌표 값 (상하좌우)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

height, width = map(int, sys.stdin.readline().split())

map_data = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(height)]

# (y, x, 벽을 부술 수 있는지 여부)를 저장하기 위한 path 선언
path = deque()
path.append((0, 0, 1))
visit_data = [[[0] * 2 for _ in range(width)] for _ in range(height)]
visit_data[0][0][1] = 1  # 시작지점 방문 초기화

while path:
    y, x, wall_state = path.popleft()

    if x == width - 1 and y == height - 1:  # 도착지점에 도착한 경우
        print(visit_data[y][x][wall_state])
        exit()

    # 현재 좌표에서 이동 가능한 상하좌우 탐색
    for move_x, move_y in directions:
        next_x, next_y = x + move_x, y + move_y

        if 0 <= next_x < width and 0 <= next_y < height:  # 다음 좌표가 범위 내에 있는 경우
            if map_data[next_y][next_x] == 1 and wall_state == 1:  # 다음 좌표가 벽이고, 벽을 부술 수 있는 경우 => 이전에 벽을 부수지 않은 경우
                visit_data[next_y][next_x][0] = visit_data[y][x][1] + 1
                path.append((next_y, next_x, 0))
            elif map_data[next_y][next_x] == 0 and visit_data[next_y][next_x][wall_state] == 0:  # 다음 좌표가 벽이 아니고, 방문하지 않은 경우
                visit_data[next_y][next_x][wall_state] = visit_data[y][x][wall_state] + 1
                path.append((next_y, next_x, wall_state))

print(-1)
