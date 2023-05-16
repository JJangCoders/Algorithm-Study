from sys import stdin

def combination(N, M):
    up = N
    down = 1
    for i in range(1, M):
        up = up * (N - i)
    for i in range(M, 0, -1):
        down *= i
    
    result = up//down

    return result

T = int(stdin.readline())

for _ in range(T):
    N, M = map(int, stdin.readline().split())

    print(combination(M, N))