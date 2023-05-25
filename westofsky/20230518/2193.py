T = int(input())
dp = [0] * (T + 1)
dp[0] = 1
dp[1] = 1
for i in range(2,T):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[T-1])