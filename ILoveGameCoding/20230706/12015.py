import sys


def binary_search(datas, target):
    start = 0
    end = len(datas) - 1

    while start <= end:
        mid = (start + end) // 2

        if datas[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return start


def solution(sequence):
    longest_sequence = [0]

    for num in sequence:
        if longest_sequence[-1] < num:
            longest_sequence.append(num)
        else:
            longest_sequence[binary_search(longest_sequence, num)] = num

    return len(longest_sequence) - 1


N = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))
print(solution(sequence))
