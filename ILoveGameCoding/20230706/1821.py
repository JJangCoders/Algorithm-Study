import sys
from itertools import permutations


def check_triangle(permutation):
    if len(permutation) == 1:  # 삼각형의 최하단에 도달했을 때 해당 값 반환
        return permutation[0]
    else:  # 삼각형의 최하단이 아닐 경우
        next_row = [permutation[idx] + permutation[idx + 1] for idx in range(len(permutation) - 1)]
        return check_triangle(next_row)


def solution(numbers_at_top, number_at_bottom):
    for permutation in permutations(range(1, numbers_at_top + 1)):  # 1부터 n까지의 순열을 구한 후 각 순열에 대해 triangle 탐색
        if check_triangle(list(permutation)) == number_at_bottom:
            return permutation


N, F = map(int, sys.stdin.readline().split())
print(" ".join(str(num) for num in solution(N, F)))
