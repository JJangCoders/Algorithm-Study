# this is my solution for BaekJoon 16924
# 십자가 찾기
# https://www.acmicpc.net/problem/16924

from sys import stdin

N, M = map(int, stdin.readline().split())
graph = [stdin.readline().strip() for _ in range(N)]

crosses = []

for i in range(1, N):
    for j in range(1, M):
        if graph[i][j] == '*':
            delta = 1
            while (i-delta) >= 0 and (i+delta) < N and (j-delta) >= 0 and (j+delta) < M:
                if graph[i][j-delta] == '*' and graph[i][j+delta] == '*' and graph[i-delta][j] == '*' and graph[i+delta][j] == '*':
                    delta += 1 
                else:
                    break
            delta -= 1
            if delta > 0:
                crosses.append((i, j, delta))

graph2 = [['.']*M for _ in range(N)]

for cross in crosses:
    i = cross[0]
    j = cross[1]
    d = cross[2]
    for delta in range(d+1):
        graph2[i][j-delta] = '*'
        graph2[i][j+delta] = '*'
        graph2[i-delta][j] = '*'
        graph2[i+delta][j] = '*'

same_flag = True

for i in range(N):
    for j in range(M):
        if graph[i][j] != graph2[i][j]:
            same_flag = False
            break
    if same_flag == False:
        break

if same_flag:
    print(len(crosses))
    for cross in crosses:
        print(cross[0]+1, cross[1]+1, cross[2])
else:
    print(-1)

