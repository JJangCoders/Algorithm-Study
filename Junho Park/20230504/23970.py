from sys import stdin

class bubbleSort:
    def __init__(self):
        self.n = int(stdin.readline())
        self.arrayA = list(map(int, stdin.readline().split()))
        self.arrayB = list(map(int, stdin.readline().split()))
        self.sameN = 0
    
    def sameNfunc(self):
        for i in range(self.n):
            if self.arrayA[i] == self.arrayB[i]:
                self.sameN += 1
    
    def sortCmp(self):
        self.sameNfunc()
        if self.sameN == self.n:
            return 1
        sortBoundary = self.n - 1
        tmpBoundary = 0
        for i in range(self.n):
            sortCnt = 0
            for j in range(sortBoundary):
                if self.arrayA[j] > self.arrayA[j+1]:
                    # swap -> makes difference?
                    if self.arrayA[j] == self.arrayB[j] and self.arrayA[j+1] == self.arrayB[j+1]:
                        self.sameN -= 2
                    elif self.arrayA[j] == self.arrayB[j] or self.arrayA[j+1] == self.arrayB[j+1]:
                        self.sameN -= 1
                    
                    tmp = self.arrayA[j]
                    self.arrayA[j] = self.arrayA[j+1]
                    self.arrayA[j+1] = tmp

                    if self.arrayA[j] == self.arrayB[j]:
                        self.sameN += 1
                    if self.arrayA[j+1] == self.arrayB[j+1]:
                        self.sameN += 1
                    
                    tmpBoundary = j
                    sortCnt += 1

                    if self.sameN == self.n:
                        return 1
            if sortCnt == 0:
                break
            sortBoundary = tmpBoundary

        return 0

bubble = bubbleSort()
result = bubble.sortCmp()

print(result)