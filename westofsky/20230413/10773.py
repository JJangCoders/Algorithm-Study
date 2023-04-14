T = int(input())
answer = []
for case in range(T):
    money = int(input())
    if money == 0:
        answer.pop()
    else:
        answer.append(money)

print(sum(answer))