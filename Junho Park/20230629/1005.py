# this is my solution for BaekJoon 1005
#
# https://www.acmicpc.net/problem/1005
#
# Reference: https://velog.io/@enchantee/%EB%B0%B1%EC%A4%80-1005-Python-kvth6jbu

from sys import stdin
from collections import deque

class ACM_Craft:
    def __init__(self):
        self.N, self.K = map(int, stdin.readline().split())
        self.times = [0] + list(map(int, stdin.readline().split()))
        self.seq = [[] for _ in range(self.N+1)]
        self.inDegree = [0 for _ in range(self.N+1)]
        self.dp = [0 for _ in range(self.N+1)]

        for _ in range(self.K):
            a, b = map(int, stdin.readline().split())
            self.seq[a].append(b)
            self.inDegree[b] += 1
        
        self.goal = int(stdin.readline())
        self.minTimeGoal()

    def minTimeGoal(self):
        q = deque()
        for i in range(1, self.N+1):
            if self.inDegree[i] == 0:
                q.append(i)
                self.dp[i] = self.times[i]
        
        while q:
            now = q.popleft()
            for block in self.seq[now]:
                self.inDegree[block] -= 1
                self.dp[block] = max(self.dp[now]+self.times[block], self.dp[block])
                if self.inDegree[block] == 0:
                    q.append(block)
        print(self.dp[self.goal])

# number of cases
T = int(stdin.readline())

for _ in range(T):
    acm = ACM_Craft()