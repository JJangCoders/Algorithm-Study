# This is my solution for BaekJoon 1697 숨바꼭질
#
# https://www.acmicpc.net/problem/1697
# 
# Reference: https://www.youtube.com/watch?v=e7_H8SLZlHY (YouTube)
# Reference: https://wook-2124.tistory.com/273

from collections import deque

# input constraint
MAX_LENGTH = 10 ** 5

class hideAndSeek:
    def __init__(self):
        self.A, self.B = map(int, input())
        self.time = [0]*(MAX_LENGTH + 1)    # array to store time to reach a point x

    def bfs(self):
        q = deque()
        q.append(self.A)
        while q:
            x = q.popleft()
            if x == self.B:
                print(self.time[x])
                break
            for nx in (x-1, x+1, x*2):
                if 0 <= nx <= MAX_LENGTH and not self.time[nx]:
                    # not time[nx] is there to prevent overriding the same place
                    self.time[nx] = self.time[x] + 1
                    q.append(nx)

sol = hideAndSeek()
sol.bfs()