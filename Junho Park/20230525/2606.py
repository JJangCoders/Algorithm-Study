# This is my solution for BaekJoon 2606 바이러스
#
# https://www.acmicpc.net/problem/2606

from sys import stdin

# My first attempt: Wrong Answer
# import heapq

# # number of computers
# N = int(stdin.readline())
# # number of connections
# K = int(stdin.readline())

# # array to store whether a computer is infected or not
# status = [0] * (N + 1)

# # computer #1 gets infected
# status[1] = 1

# # array to store connection information
# conn = []

# for _ in range(K):
#     ab = list(map(int, stdin.readline().split()))
#     ab.sort()
#     a = ab[0]
#     b = ab[1]
#     heapq.heappush(conn, (a, b))

# while conn:
#     a, b = heapq.heappop(conn)
#     status[b] = status[a]

# print(sum(status)-1)

# number of computers
N = int(stdin.readline())
# number of connections
K = int(stdin.readline())

graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)

for _ in range(K):
    A, B = map(int, stdin.readline().split())
    graph[A].append(B)
    graph[B].append(A)

def DFS(v):
    visited[v] = 1
    for u in graph[v]:
        if visited[u] == 0:
            DFS(u)

DFS(1)

print(sum(visited) - 1)