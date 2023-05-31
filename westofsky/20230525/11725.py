import sys
sys.setrecursionlimit(10**6)
T = int(sys.stdin.readline())
graph = [[] for _ in range(T+1)]
visited = [False] * (T+1)
parent = [0] * (T+1)

for _ in range(T-1):
    start,end = map(int,sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)
for i in range(T+1):
    graph[i].sort()
def DFS(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            parent[i] = v
            DFS(i)
DFS(1)
for i in range(2,T+1):
    print(parent[i])