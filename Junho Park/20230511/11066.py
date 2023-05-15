# This is my solution for BaekJoon 11066
#
# https://www.acmicpc.net/problem/11066
#
# Reference: https://velog.io/@ledcost/%EB%B0%B1%EC%A4%80-11066-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%8C%8C%EC%9D%BC-%ED%95%A9%EC%B9%98%EA%B8%B0-%EA%B3%A8%EB%93%9C3-DP

from sys import stdin

# number of test cases
T = int(stdin.readline())

for _ in range(T):
    # number of chapters
    N = int(stdin.readline())

    # lengths of each chapter
    chapters = list(map(int, stdin.readline().split()))

    # array to store local minimum costs
    # minimum cost of the range (a, b) -> minCost[a][b]
    minCost = [[0]*N for _ in range(N)]

    # dictionary to store sum to use later
    # sum of copies until k -> subSum[k]
    subSum = {-1: 0}
    for i in range(N):
        subSum[i] = subSum[i-1] + chapters[i]
    
    # loop to calculate local minimum costs
    for size in range(1, N):
        for start in range(N-1):
            end = start + size

            if end >= N:
                break
            
            # variable to store a local minimum cost between (start, end)
            localMin = float("inf")

            # loop to determine minimum local cost between (start, end)
            # each loop, it compares which one of slices (start, slice), (slice + 1, end)
            # as a result, the slice that makes the minimum cost will be stored at localMin
            for boundary in range(start, end):
                localMin = min(localMin, minCost[start][boundary] + minCost[boundary+1][end] + subSum[end] - subSum[start-1])
            
            # saving the local minimum cost
            minCost[start][end] = localMin
    
    print(minCost[0][N - 1])