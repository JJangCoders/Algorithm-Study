# This is my solution for BaekJoon 1697 숨바꼭질
#
# https://www.acmicpc.net/problem/1697

from collections import deque

def bfs():
    q = deque()
    q.append(A)
    while q:
        x = q.popleft()
        if x == B:
            print(time[x])
            break
        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= MAX_LENGTH and not time[nx]:
                # not time[nx] is there to prevent overriding the same place
                time[nx] = time[x] + 1
                q.append(nx)


A, B = map(int, input().split())

# input constraint
MAX_LENGTH = 10 ** 5

# time needed to reach from a to b
time = [0]*(MAX_LENGTH + 1)

bfs()