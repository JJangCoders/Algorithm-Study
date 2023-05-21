# This is my solution for BaekJoon 1965
#
# https://www.acmicpc.net/problem/1965
#
# Reference: https://alpyrithm.tistory.com/91
from sys import stdin

N = int(stdin.readline())

box = list(map(int, stdin.readline().split()))

dp = [1 for _ in range(N)]

for i in range(1, N):
    for j in range(i):
        if box[i] > box[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))