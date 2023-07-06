import sys
T = int(sys.stdin.readline())
maps = []
visited = [[False] * T for _ in range(T)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for _ in range(T):
    maps.append(list(sys.stdin.readline().strip()))

answer1 = 0
answer2 = 0
def chkRange(x,y):
    return 0 <= x and x < T and 0 <= y and y < T
def dfs(x,y):
    visited[x][y] = True
    now_color = maps[x][y]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if chkRange(nx,ny):
            if visited[nx][ny] == False: #첫방문
                if maps[nx][ny] == now_color:
                    dfs(nx,ny)

for i in range(T):
    for j in range(T):
        if visited[i][j] == False:
            dfs(i,j)
            answer1 += 1
for i in range(T):
    for j in range(T):
        if maps[i][j] == "G":
            maps[i][j] = "R"
visited = [[False] * T for _ in range(T)]
for i in range(T):
    for j in range(T):
        if visited[i][j] == False:
            dfs(i,j)
            answer2 += 1

print(answer1,answer2)