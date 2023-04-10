from sys import stdin

n = int(stdin.readline())

numbers = []

for i in range(n):
    number = int(stdin.readline())

    if number == 0:
        del numbers[len(numbers) - 1]
    else:
        numbers.append(number)

sum = 0

for number in numbers:
    sum += number

print(sum)