import sys
import heapq

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    start , end , w = map(int,sys.stdin.readline().split())
    graph[start].append((end,w))
answer_start , answer_end = map(int,input().split())

weight = [float('inf')] * (n+1)
weight[answer_start] = 0

heap = [(0,answer_start)] 
while(heap):
    now_weight, now_des = heapq.heappop(heap)
    if weight[now_des] < now_weight:
        continue
    for node in graph[now_des]:
        w = now_weight + node[1]
        if weight[node[0]] > w:
            weight[node[0]] = w
            heapq.heappush(heap,(w,node[0]))

print(weight[end])