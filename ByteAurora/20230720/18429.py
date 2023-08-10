import sys
from itertools import permutations


def is_valid(current, exercise_kits, decrease_amount):
    if len(exercise_kits) == 0:
        return True

    current += (exercise_kits[0] - decrease_amount)
    return current >= 500 and is_valid(current, exercise_kits[1:], decrease_amount)


def solution(exercise_kits, decrease_amount):
    valid_count = 0

    for permutation in permutations(exercise_kits):  # 1부터 n까지의 순열을 구한 후 각 순열에 대해 triangle 탐색
        if is_valid(500, permutation, decrease_amount):
            valid_count += 1

    return valid_count


N, K = map(int, sys.stdin.readline().split())
exercise_kits = list(map(int, sys.stdin.readline().split()))

print(solution(exercise_kits=exercise_kits, decrease_amount=K))
