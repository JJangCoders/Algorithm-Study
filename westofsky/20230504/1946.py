import sys
T =int(sys.stdin.readline())
for i in range(T):
    n = int(sys.stdin.readline())
    answer = 1
    employ = []
    for j in range(n):
        temp = list(map(int,sys.stdin.readline().split()))
        employ.append(temp)
    employ.sort(key= lambda x : x[0])
    maxEmploy = 0
    for k in range(1,n):
        if employ[k][1] < employ[maxEmploy][1]:
            maxEmploy = k
            answer += 1
    print(answer)
