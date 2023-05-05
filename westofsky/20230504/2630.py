import sys
T = int(input())
answer = []
def halfMap(pos_x,pos_y,lens):
    colors = maps[pos_x][pos_y]
    for i in range(pos_x,pos_x+lens):
        for j in range(pos_y,pos_y+lens):
            if colors != maps[i][j]:
                newLens = lens // 2
                halfMap(pos_x,pos_y,newLens)
                halfMap(pos_x,pos_y+newLens,newLens)
                halfMap(pos_x+newLens,pos_y,newLens)
                halfMap(pos_x+newLens,pos_y+newLens,newLens)
                return

    if colors == 1:
        answer.append(1)
    else:
        answer.append(0)

maps = [list(map(int,sys.stdin.readline().split())) for _ in range(T)]
halfMap(0,0,T)
print(answer.count(0))
print(answer.count(1))