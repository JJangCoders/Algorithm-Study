# This is my solution for BaekJoon 1946 problem
#
# https://www.acmicpc.net/problem/1946 

from sys import stdin
import heapq

T = int(stdin.readline())

for z in range(T):
    N = int(stdin.readline())

    # number of candidates passing, first one always passes
    pass_cnt = 1

    scores = []

    for i in range(N):
        paper, interview = map(int, stdin.readline().split())
        heapq.heappush(scores, (paper, interview))

    paper, interview = heapq.heappop(scores)
    interviewT = interview
    # 1st rank in paper sets standard for the following candidates
    
    while len(scores) > 0:
        paper, interview = heapq.heappop(scores)
        if interview <= interviewT:
            pass_cnt += 1
            interviewT = interview
            # interview standard update

    print(pass_cnt)