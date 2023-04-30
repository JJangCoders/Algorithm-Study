import sys
from heapq import heappush, heappop

input_count = int(input())
heap = []

for i in range(0, input_count):
    input_value = int(sys.stdin.readline().strip())  # input() 쓰니까 시간초과 나옴
    if input_value != 0:
        heappush(heap, (abs(input_value), input_value))  # 절대값이 작은 순으로 정렬해서 추가
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(heappop(heap)[1])  # [0]에는 절대값 [1]에는 원래 값
