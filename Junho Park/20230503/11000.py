# This is my solution for BaekJoon 11000 problem
#
# https://www.acmicpc.net/problem/11000

from sys import stdin
import heapq

N = int(stdin.readline())

classTime = []

endTime = []

for i in range(N):
    S, T = map(int, stdin.readline().split())
    heapq.heappush(classTime, (S, T))
# input

# My first attempt: Timeout, Wrong Answer
# while len(classTime) > 0:
#     S, T = heapq.heappop(classTime)

#     isAvaliable = False

#     for i in range(len(classRegister)):
#         if classRegister[i][1]<=S:
#             isAvaliable = True
    
#     if isAvaliable:
#         heapq.heappop(classRegister)
#         heapq.heappush(classRegister, (S, T))
#     else:
#         heapq.heappush(classRegister, (S, T))

# print(len(classRegister))

# My second attempt: Timeout
# S, T = heapq.heappop(classTime)
# endTime.append(T)

# while len(classTime) > 0:
#     S, T = heapq.heappop(classTime)

#     moreClass = True
#     endTimeLength = len(endTime)
#     for i in range(endTimeLength):
#         if endTime[i] <= S:
#             moreClass = False
#             endTime[i] = T
#             break
#     if moreClass:
#         endTime.append(T)

# print(len(endTime))

# My third attempt
# Referenced: https://hongcoding.tistory.com/79

_, T = heapq.heappop(classTime)

heapq.heappush(endTime, T)

for i in range(1, N):
    S, T = heapq.heappop(classTime)
    if S < endTime[0]:
        heapq.heappush(endTime, T)
    else:
        heapq.heappop(endTime)
        heapq.heappush(endTime, T)
print(len(endTime))