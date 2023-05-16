# This is my solution for BaekJoon 14501
# 
# https://www.acmicpc.net/problem/14501

from sys import stdin

# number of days he will work
N = int(stdin.readline())

# list of tuples to store (day, length, profit) of consults
consults = []

# loop N times
for i in range(N):
    length, profit = map(int, stdin.readline().split())

    # can't do it, skip
    if i + length >= N:
        continue

    consults.append((i+1, length, profit))

# number of possible consults
L = len(consults)