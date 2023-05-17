n = int(input())

# 0 ~ 9까지 총 10개, N개의 자릿수
dp = [[0] * 10 for _ in range(n + 1)]

# 한 자릿수는 1로 초기화
for i in range(1, 10):
    dp[1][i] = 1

for digit in range(2, n + 1):
    for num in range(10):
        if num == 0:  # 0일 때는 1만 가능
            dp[digit][num] = dp[digit - 1][1]
        elif num == 9:  # 9일 때는 8만 가능
            dp[digit][num] = dp[digit - 1][8]
        else:  # 1 ~ 8일 때는 +1, -1 두 값이 가능
            dp[digit][num] = dp[digit - 1][num - 1] + dp[digit - 1][num + 1]

print(sum(dp[n]) % 1_000_000_000)
