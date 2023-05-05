import heapq
import sys
T = int(input())
studies = []
endPoint = []
answer = 1
for t in range(T):
    studies.append(list(map(int,sys.stdin.readline().split())))
studies.sort()
heapq.heappush(endPoint,studies[0][1])
for i in range(1,T):
    if answer < len(endPoint):
        answer = len(endPoint)
    start,end = studies[i]
    if start >= endPoint[0]:
        heapq.heappop(endPoint)
        heapq.heappush(endPoint,end)
    else:
        heapq.heappush(endPoint,end)
if answer < len(endPoint):
    answer = len(endPoint)

print(answer)