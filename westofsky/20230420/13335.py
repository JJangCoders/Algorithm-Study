from collections import deque
import sys
n,l,w = map(int,sys.stdin.readline().split())
in_bridge = 0
trucks = list(map(int,sys.stdin.readline().split()))
trucks.reverse()
time = 0
bridge = deque()
in_time = deque()
while len(trucks) !=0 or len(bridge) != 0:
    time += 1
    for idx in range(len(in_time)):
        in_time[idx] += 1
    if len(in_time) != 0:
        if in_time[0] > l:
            in_time.popleft()
            in_bridge -= bridge.popleft()
    if len(trucks) != 0:
        if trucks[-1] + in_bridge <= w:
            truck = trucks.pop()
            bridge.append(truck)
            in_time.append(1)
            in_bridge += truck

print(time)

