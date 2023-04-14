N, M = map(int, input().split())
posY, posX, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
clean = 0
isRunning = True
dy = (-1, 0, 1, 0)
dx = (0, -1, 0, 1)


def is_wall(y, x):
    if room[y][x] == 1:
        True
    else:
        False


def is_not_clean(y, x):
    clean = True
    for i in range(4):
        if is_wall(y + dy[i], x + dx[i]):
            continue
        else:
            if room[y + dy[i]][x + dx[i]] == 0:
                clean = False
    return clean


# 0이 북쪽 1이 동쪽 2가 남쪽 3이 서쪽
while isRunning:
    if room[posY][posX] == 0:
        room[posY][posX] = 2
        clean += 1
    # 청소되지 않은 빈 칸이 없는 경우
    if is_not_clean(posY, posX):
        # 바라보는 방향의 뒤이니까
        if room[posY + (-1) * direction[d][0]][posX + (-1) * direction[d][1]] == 1:
            isRunning = False
        else:
            posY += (-1) * direction[d][0]
            posX += (-1) * direction[d][1]
    else:
        if d == 0:
            d = 3
        else:
            d -= 1
        if room[posY + direction[d][0]][posX + direction[d][1]] == 0:
            posY += direction[d][0]
            posX += direction[d][1]

print(clean)