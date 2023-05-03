#
import sys
import heapq

class_count = int(input())
classes = []

for _ in range(class_count):
    classes.append(list(map(int, sys.stdin.readline().split())))  # input()으로 받으니까 시간 초과 남
classes.sort(key=lambda x: x[0])

classrooms = []

for start_time, end_time in classes:
    if classrooms and classrooms[0] <= start_time:  # 현재 강의실에서 진행 중인 강의 중 가장 빨리 끝나는 강의 시간이 새롭게 진행할 강의 시작 시간보다 빨리 끝날 경우
        heapq.heappop(classrooms)  # 강의실에서 진행 중인 강의 중 가장 빨리 끝나는 강의 종료

    heapq.heappush(classrooms, end_time)  # 새롭게 진행할 강의를 강의실에 추가

print(len(classrooms))
