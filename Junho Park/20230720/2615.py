# This is my solution for BaekJoon 2615
# 오목
# https://www.acmicpc.net/problem/2615

from sys import stdin

def check_omok(i, j):
    color = board[i][j]
    dx = [-1, 0, 1, 1]
    dy = [1, 1, 1, 0]

    for k in range(4):
        x = i
        y = j
        cnt = 1 # matching streak

        while True:
            x += dx[k]
            y += dy[k]

            if x < 0 or y < 0 or x > 18 or y > 18:
                break
            
            if board[x][y] == color:
                cnt += 1
            else:
                break
            
            if cnt == 5:
                before_x = i - dx[k]
                before_y = j - dy[k]

                after_x = x + dx[k]
                after_y = y + dy[k]

                if before_x < 0 or before_y < 0 or before_x > 18 or before_y > 18:
                    before_flag = False
                else:
                    if board[before_x][before_y] == color:
                        before_flag = True
                    else:
                        before_flag = False
                
                if after_x < 0 or after_y < 0 or after_x > 18 or after_y > 18:
                    after_flag = False
                else:
                    if board[after_x][after_y] == color:
                        after_flag = True
                    else:
                        after_flag = False
                
                if before_flag or after_flag:
                    break
                else:
                    return color
    return 0
# -- input --
# 0 -> blank, 1 -> black, 2 -> white
# 19 x 19 size omok board
board = [list(map(int, stdin.readline().split())) for _ in range(19)]

# check flag
# 0 -> no check, 1 -> check
chk = [[0] * 19 for _ in range(19)]

break_flag = False

for i in range(19):
    if break_flag:
        break
    for j in range(19):
        if board[i][j] == 0:
            #blank space
            pass
        else:
            if check_omok(i, j) != 0:
                print(board[i][j])
                print(i+1, j+1)
                break_flag = True
                break

if break_flag == False:
    print(0)