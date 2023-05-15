# This is my solution for BaekJoon 9251
#
# https://www.acmicpc.net/problem/9251

from sys import stdin

def LCSLength(s1, s2):
    m = len(s1)
    n = len(s2)

    # creating table (m+1) x (n+1) size
    table = [[0] * (n+1) for _ in range(m+1)]

    # propagation loop
    for i in range(1, m + 1):
        for j in range(1, n + 1):

            # I remember this kind of thing from my Algorithm course at uni
            # A professor from India was explaining how this works
            if s1[i - 1] == s2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])
    
    return table[m][n]

# input: 2 sentences (All Capital English Alphabet Letters)
s1 = stdin.readline().strip()
s2 = stdin.readline().strip()

print(LCSLength(s1, s2))