import sys
T = int(sys.stdin.readline())
graph = [[] for i in range(T+1)]
visited = [False] * (T+1)
C = int(sys.stdin.readline())
for _ in range(C):
    start, end = map(int,sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)

def DFS(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            DFS(i)
DFS(1)
print(visited.count(True)-1)
