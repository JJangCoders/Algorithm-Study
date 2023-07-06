# This is my solution for BaekJoon 1821 수들의 합 6
# 
# https://www.acmicpc.net/problem/1821

# my initial approach
#
# def pascal(N, F):
#     if N == 1:
#         return
#     for i in range(1, F):
#         pascal(N-1, i)
#         pascal(N-1, F-i)

N, F = map(int, input().strip().split())

