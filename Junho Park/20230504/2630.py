# This is my solution for BaekJoon 2630
# 
# https://www.acmicpc.net/problem/2630

from sys import stdin

class Orgami:
    def __init__(self):
        # input 
        self.N = int(stdin.readline())
        self.orgami = []
        for i in range(self.N):
            self.orgami.append(list(map(int, stdin.readline().split())))
        
        # array for the numbers of each color orgami
        self.colors = [0, 0]

    def cut(self, orgami):
        N = len(orgami)
        if self.isOneColor(orgami, N):
            self.colors[orgami[0][0]] += 1
        else:
            part1 = []
            part2 = []
            part3 = []
            part4 = []

            # part 1, part 2 slcing
            for i in range(N//2):
                part1.append(orgami[i][:N//2])
                part2.append(orgami[i][N//2:])
            
            #part 3, part 4 slicing
            for i in range(N//2, N):
                part3.append(orgami[i][:N//2])
                part4.append(orgami[i][N//2:])
            
            self.cut(part1)
            self.cut(part2)
            self.cut(part3)
            self.cut(part4)

    def isOneColor(self, orgami, N):
        color = orgami[0][0]
        for i in range(N):
            for j in range(N):
                if orgami[i][j] != color:
                    return False
        return True

orgami = Orgami()
orgami.cut(orgami.orgami)
print(orgami.colors[0])
print(orgami.colors[1])