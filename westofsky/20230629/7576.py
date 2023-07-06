import sys
from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs():
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < N and 0 <= ny < M:
                if graph[nx][ny]==0:
                    q.append([nx,ny])
                    graph[nx][ny]=graph[x][y]+1

q=deque([])
M, N = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if graph[i][j]==1:
            q.append([i,j])
            
bfs()
answer = 0
for i in graph:
    for j in i:
        if j==0:
            print(-1)
            exit(0)
    answer = max(answer, max(i))

print(answer-1)