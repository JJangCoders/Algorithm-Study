import sys

result = 0
num_list = []

for _ in range(0, int(sys.stdin.readline())):
    current_num = int(sys.stdin.readline())
    if current_num:
        result += current_num
        num_list.append(current_num)
        continue

    result -= num_list.pop()

print(result)
