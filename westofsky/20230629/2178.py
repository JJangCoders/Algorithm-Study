import sys
from collections import deque
answer = 0
X,Y = map(int,sys.stdin.readline().split())
maps = []
for i in range(X):
    maps.append(list(map(int,sys.stdin.readline().strip())))
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]): continue

            if maps[nx][ny] == 0:
                continue

            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))

    return maps[len(maps)-1][len(maps[0])-1]
print(bfs(0,0))