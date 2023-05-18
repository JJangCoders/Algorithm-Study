n = int(input())

# 2차원 배열 풀이
# dp = [[0] * 2 for _ in range(n + 1)]
# if n < 3:
#     print(1)
# else:
#     dp[1][1] = 1
#
#     for digit in range(2, n+1):
#         dp[digit][0] = dp[digit-1][0] + dp[digit-1][1]
#         dp[digit][1] = dp[digit-1][0]
#
#     print(sum(dp[n]))
#
#    0 1
# 0  0 0   0
# 1  0 1   1
# 2  1 0   1
# 3  1 1   2
# 4  2 1   3
# 5  3 2   5

# 1차원 배열 풀이
dp = [0] * (n + 1)
if n < 3:
    print(1)
else:
    dp[1] = 1

    for digit in range(2, n+1):
        dp[digit] = dp[digit-1] + dp[digit-2]

    print(dp[n])

# 현재 자릿수가 0이라면 이전 자릿수는 0, 1 둘 다 가능
# 현재 자릿수가 1이라면 이전 자릿수는 0만 가능
# dp[digit-1]은 현재 자릿수의 값이 0일 때
# dp[digit-2]는 현재 자릿수의 값이 1일 때
# dp[0] = 0
# dp[1] = 1
# dp[2] = 1
# dp[3] = 2
# 1 0 1
# 1 0 0