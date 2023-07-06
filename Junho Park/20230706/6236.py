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

# Reference: https://velog.io/@deannn/BOJ-%EB%B0%B1%EC%A4%80-6236-%EC%9A%A9%EB%8F%88%EA%B4%80%EB%A6%AC-Python

N, M = map(int, stdin.readline().split())
money = []  # money for each day
for _ in range(N):
    money.append(int(stdin.readline()))

# Two pointers
left = min(money)
right = sum(money)

while left <= right:
    mid = (left + right) // 2   # center value, temporary K
    balance = mid               # cashing out
    cnt = 1                     # cashing out count

    for pay in money:
        if balance < pay:
            balance = mid
            cnt += 1
        balance -= pay
    
    if cnt > M or mid < max(money):
        left = mid + 1
    else:
        right = mid - 1
        K = mid

print(K)