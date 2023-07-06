# This is my solution for BaekJoon 6236
# 용돈 관리
# https://www.acmicpc.net/problem/6236

from sys import stdin

# =================================================
# My initial solution -> timeout
# =================================================
# class solution:
#     def __init__(self):
#         self.N, self.M = map(int, stdin.readline().split())
#         self.money = []
#         for _ in range(self.N):
#             self.money.append(int(stdin.readline()))
#         self.minMoney = min(self.money)
#         self.maxMoney = max(self.money)
#         self.K = self.maxMoney
#         self.solve()

#     def solve(self):
#         wdc = self.withdrawCount()
#         while True:
#             if wdc == self.M:
#                 print(self.K)
#                 return
#             else:
#                 if wdc > self.M:
#                     self.K += 1
#                 else:
#                     self.K -= 1
#                 wdc = self.withdrawCount()
    
#     def withdrawCount(self):
#         cnt = 0
#         balance = 0
#         for money in self.money:
#             if balance < money:
#                 cnt += 1
#                 balance = self.K
#             balance -= money
#             while balance < 0:
#                 cnt += 1
#                 balance += self.K
#         return cnt

# sol = solution()

