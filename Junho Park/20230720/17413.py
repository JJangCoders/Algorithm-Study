# this is my solution for BaekJoon 17413
# 단어 뒤집기 2
# https://www.acmicpc.net/problem/17413

from sys import stdin

sentence = stdin.readline().strip()

index = 0
tmp_word = ""
reversed_sentence = ""

strlen = len(sentence)

while index < strlen:
    tmp_word = ""
    if sentence[index] == '<':
        while sentence[index] != '>':
            reversed_sentence += sentence[index]
            index += 1
        reversed_sentence += sentence[index]
        index += 1
    elif sentence[index] == ' ':
        reversed_sentence += ' '
        index += 1
    else:
        while index < strlen and (sentence[index] != ' ' and sentence[index] != '<'):
            tmp_word += sentence[index]
            index += 1
        reversed_sentence += tmp_word[::-1]

print(reversed_sentence)