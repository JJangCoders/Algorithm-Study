import sys

Y,X = map(int,sys.stdin.readline().split())

graph = [[False] * (X) for _ in range(Y)]
maps = []
answer = 0
def checkRange(i,j):
    return i >=0 and i < Y and j>=0 and j<X
def DFS(i,j,t):
    graph[i][j] = True
    if t == '-':
        if not checkRange(i,j+1):
            pass
        else:
            if t == maps[i][j+1]:
                DFS(i,j+1,t)
    elif t == '|':
        if not checkRange(i+1,j):
            pass
        else:
            if t == maps[i+1][j]:
                DFS(i+1,j,t)

for i in range(Y):
    maps.append(list(input()))
for i in range(Y):
    for j in range(X):
        if not graph[i][j]: #다른 블럭에 포함이 안됐을때
            answer += 1
            DFS(i,j,maps[i][j])

print(answer)