from sys import stdin

def cleaning(matrix, N, M, r, c, d):

    cleaning_cnt = 0

    while(True):
        if matrix[r][c] == 0:   #current spot dirty
            matrix[r][c] = 2    #cleaning
            cleaning_cnt += 1
        else:                   #current spot clean
            if matrix[r - 1][c] != 0 and matrix[r][c + 1] != 0 and matrix[r + 1][c] and matrix[r][c - 1] != 0:  #there is no place to clean around the robot
                if d == 0:      #facing north
                    if matrix[r + 1][c] != 1:   #no wall behind
                        r = r + 1
                        continue
                    else:                       #wall behind
                        break
                elif d == 1:      #facing east
                    if matrix[r][c - 1] != 1:   #no wall behind
                        c = c - 1
                        continue
                    else:                       #wall behind
                        break
                elif d == 2:      #facing south
                    if matrix[r - 1][c] != 1:   #no wall behind
                        r = r - 1
                        continue
                    else:                       #wall behind
                        break
                elif d == 3:      #facing west
                    if matrix[r][c + 1] != 1:   #no wall behind
                        c = c + 1
                        continue
                    else:                       #wall behind
                        break
            else:           #there is place to clean around the robot
                forward_clean = 1
                while(forward_clean):   #rotating the robot until the forward spot is dirty
                    d -= 1
                    if d < 0:
                        d = 3
                    #rotating the robot counter-clock wise

                    if d == 0:      #facing north
                        if matrix[r - 1][c] == 0:
                            forward_clean = 0
                            r = r - 1
                    elif d == 1:    #facing east
                        if matrix[r][c + 1] == 0:
                            forward_clean = 0
                            c = c + 1
                    elif d == 2:    #facing south
                        if matrix[r + 1][c] == 0:
                            forward_clean = 0
                            r = r + 1
                    elif d == 3:    #facing west
                        if matrix[r][c - 1] == 0:
                            forward_clean = 0
                            c = c - 1
    return cleaning_cnt

        

N, M = map(int, stdin.readline().split())

r, c, d = map(int, stdin.readline().split())

'''
    switch(d)
        case 0 : North
        case 1 : East
        case 2 : South
        case 3 : West
'''

cleaning_space = []

for i in range(N):
    cleaning_space.append(list(map(int, stdin.readline().split())))

print(cleaning(cleaning_space, N, M, r, c, d))