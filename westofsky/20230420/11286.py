# #시간초과
# T = int(input())
# answer = []
# for i in range(T):
#     inputs = int(input())
#     if inputs != 0:
#         answer.append(inputs)
#         answer.sort(key = lambda x : (abs(x),x))
#     else:
#         if len(answer) == 0:
#             print(0)
#         else:
#             k = answer.pop(0)
#             print(k)
import heapq
import sys
aheap = []
T = int(sys.stdin.readline())
for i in range(T):
    inputs = int(sys.stdin.readline())
    if inputs != 0:
        heapq.heappush(aheap,(abs(inputs),inputs))
    else:
        if len(aheap) == 0:
            print(0)
        else:
            _,k = heapq.heappop(aheap)
            print(k)
