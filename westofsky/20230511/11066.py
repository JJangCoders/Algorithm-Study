import sys
import math
T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    arr = list(map(int,sys.stdin.readline().split()))

    cumsum = {-1:0}

    for i in range(len(arr)):
        cumsum[i] = cumsum[i-1] + arr[i]

    dp = [[0] * len(arr) for _ in range(len(arr))]

    for gap in range(1, len(arr)):
        for start in range(len(arr)):
            end = start + gap

            if end == len(arr):
                break
            dp[start][end] = math.inf
            for i in range(start,end):
                dp[start][end] = min(dp[start][end],
                                     dp[start][i] + dp[i+1][end] + cumsum[end] - cumsum[start-1]
                                     )
    print(dp[0][-1])