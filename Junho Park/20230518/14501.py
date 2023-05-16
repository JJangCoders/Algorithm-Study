# This is my solution for BaekJoon 14501
# 
# https://www.acmicpc.net/problem/14501
#
# Reference: https://great-park.tistory.com/48

from sys import stdin

# number of days he will work
N = int(stdin.readline())

# list of tuples to store (length, profit) of consults
consults = []

# loop N times
for i in range(N):
    length, profit = map(int, stdin.readline().split())

    # can't do it, skip
    consults.append((length, profit))

# array to store maximum cost
maxCost = [0 for _ in range(N+1)]

for i in range(N):
    for j in range(i+consults[i][0], N+1):
        if maxCost[j] < maxCost[i] + consults[i][1]:
            maxCost[j] = maxCost[i] + consults[i][1]

print(maxCost[-1])