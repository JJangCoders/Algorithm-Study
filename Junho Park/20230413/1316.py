def is_group(word):
    length = len(word)
    checked_alphabets = []
    for i in range(length):
        if checked_alphabets.count(word[i]) != 0:
            continue
        for j in range(i+1, length):
            if word[i] == word[j] and word[j] != word[j-1]:
                return False
        checked_alphabets.append(i)
    return True
        

n = int(input())

cnt = 0

for i in range(n):
    word = input()

    if is_group(word):
        cnt += 1
print(cnt)