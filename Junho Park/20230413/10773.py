from sys import stdin

n = int(stdin.readline())

numbers = []    #array to store input numbers

for i in range(n):
    number = int(stdin.readline())  #input number

    if number == 0:
        del numbers[len(numbers) - 1]   #removing the last element of the array
    else:
        numbers.append(number)      #adding the number in the end

sum = 0

for number in numbers:      #loop to sum up the numbers
    sum += number

print(sum)     #output