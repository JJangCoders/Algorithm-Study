import sys


def check_group_word(word):
    group = {}
    before_ch = '0'

    for ch in word:
        if before_ch != ch:
            if ch in group:
                return False

            group[ch] = 1
            before_ch = ch

    return True


result = 0

for i in range(0, int(sys.stdin.readline())):
    result += 1 if check_group_word(sys.stdin.readline()) else 0

print(result)
