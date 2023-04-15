T = int(input())
answer = []
for words in range(T):
    word = input()
    is_word = True
    for idx in range(len(word)-1):
        if word[idx] == word[idx+1]:
            pass
        elif word[idx] in word[idx+1:]:
            is_word = False
            break

    if is_word:
        answer.append(word)
    
print(len(answer))
