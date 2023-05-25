import math
T = int(input())

for _ in range(T):
    a,b = map(int,input().split())
    answer = math.comb(b,a)
    print(answer)