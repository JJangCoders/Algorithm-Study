from collections import deque
import sys
T = int(sys.stdin.readline())
maps1 = []
maps2 = []

for i in range(T):
    inputs = sys.stdin.readline().strip()
    maps1.append(list(inputs))
    maps2.append(list(inputs.replace('G','R')))

def dfs(x,y):
