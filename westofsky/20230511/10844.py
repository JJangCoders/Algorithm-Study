T = int(input())
digits = [[0] * 10 for _ in range(T)]

digits[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for i in range(1, T):
    digits[i][0] = digits[i-1][1]
    digits[i][9] = digits[i-1][8]
    for j in range(1, 9):
        digits[i][j] = (digits[i-1][j-1] + digits[i-1][j+1]) % 1000000000

print(sum(digits[T-1])% 1000000000)