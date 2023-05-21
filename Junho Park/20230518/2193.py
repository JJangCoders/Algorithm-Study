# This is my solution for BaekJoon 2193
#
# https://www.acmicpc.net/problem/2193

N = int(input())

# array to store number of pinary number
cnt = [0 for _ in range(N+1)]

if N>2:
    cnt[1] = 1
    cnt[2] = 1
    for i in range(3, N+1):
        cnt[i] = cnt[i-1] + cnt[i-2] 

    print(cnt[-1])
else:
    print(1)
    
# 1

# 10

# 100
# 101

# 1000
# 1001
# 1010

# 10000
# 10001
# 10010
# 10100
# 10101

# 100000
# 100001
# 100010
# 100100
# 100101
# 101000
# 101001
# 101010