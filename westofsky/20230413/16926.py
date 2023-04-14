# 1차시도 코드 -> 시간초과
def prints(maps):
    for i in range(N):
        for j in range(M):
            print(maps[i][j], end=' ')
        print()
N,M,r = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
short = N if N <= M else M
for _ in range(r):
    temp = [[0]*M for _ in range(N)]
    p_1 = (0,0)
    p_2 = (0,M-1)
    p_3 = (N-1,M-1)
    p_4 = (N-1,0)
    for _ in range(short): #대각선 꼭짓점의 y값이 안 마주칠때
        for i in range(p_1[1], p_3[1]):  # 맨 위 한줄
            temp[p_1[0]][i] = arr[p_1[0]][i + 1]
        for i in range(p_1[0], p_4[0]):  # 왼쪽 한줄
            temp[i + 1][p_1[1]] = arr[i][p_1[1]]
        for i in range(p_4[1], p_3[1]): # 아래 한줄
            temp[p_4[0]][i + 1] = arr[p_4[0]][i]
        for i in range(p_2[0], p_3[0]): #오른쪽 한줄
            temp[i][p_2[1]] = arr[i + 1][p_2[1]]
        p_1 = (p_1[0] + 1, p_1[1] + 1)
        p_2 = (p_2[0] + 1, p_2[1] - 1)
        p_3 = (p_3[0] - 1, p_3[1] - 1)
        p_4 = (p_4[0] - 1, p_4[1] + 1)
    arr = list(temp)
prints(arr)

