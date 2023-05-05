import sys
N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
B = list(map(int,sys.stdin.readline().split()))
answer = 0
def sol():
    finished = N-1
    if A == B:
        print(1)
        return
    for i in range(N,1,-1):
        changed = 0
        for j in range(0,finished):
            if A[j] > A[j+1]:
                changed = 1
                temp = A[j+1]
                A[j+1] = A[j]
                A[j] = temp
                if A[j+1] == B[j+1]:
                    if A==B:
                        print(1)
                        return
        if not changed:
            break
    print(0)

sol()

