# this is my solution for BaekJoon 18429
# 근손실
# https://www.acmicpc.net/problem/18429

from sys import stdin
from itertools import permutations

N, K = map(int, stdin.readline().split())
kits = list(map(int, stdin.readline().split()))

prob_cnt = 0

for permu_kit in permutations(kits):
    big3 = 500
    valid_flag = True
    for kit in permu_kit:
        big3 += (kit - K)
        if big3 < 500:
            valid_flag = False
            break
    
    if valid_flag:
        prob_cnt += 1

print(prob_cnt)