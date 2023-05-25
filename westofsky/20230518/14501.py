import sys
T = int(sys.stdin.readline())
couns = []
for _ in range(T):
    couns.append(tuple(map(int,sys.stdin.readline().split())))

dp = [0] * T

for i in range(0,T):
    max_p = 0
    for j in range(0,i):
        if couns[j][0]+j > i or couns[j][0] + j > T-1:
            pass
        else:
            if max_p < dp[j]:
                max_p = dp[j]
    if max_p == 0:
        if couns[i][0] + i >T:
            dp[i] = 0
        else:
            dp[i] = couns[i][1]
    else:
        if i + couns[i][0] > T:
            dp[i] = max_p
        else:
            dp[i] = max_p + couns[i][1]

print(max(dp))

