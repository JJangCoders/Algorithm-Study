# This is my solution for BaekJoon 1450
# 냅색문제
# https://www.acmicpc.net/problem/1450

# Reference: https://velog.io/@dark6ro/%EB%B0%B1%EC%A4%80-1450%EB%B2%88-%EB%83%85%EC%83%89%EB%AC%B8%EC%A0%9C

from sys import stdin
from itertools import combinations

# MITM (Meet in the middle) Algorithm
def solution(N,C,m):
	if N == 1 and m[0] <= C:
		return 2
	if N == 1 and m[0] > C:
		return 1

	left_m,right_m = m[:N//2], m[N//2:]
	sub_left,sub_right = [0],[0]
	
	for i in range(1,len(left_m)+1):
		for sub in combinations(left_m,i):
			sub_left.append(sum(sub))
	sub_left = sorted(sub_left)

	for i in range(1,len(right_m)+1):
		for sub in combinations(right_m,i):
			sub_right.append(sum(sub))
	sub_right = sorted(sub_right)
	answer = 0
	for i in sub_right:
		if i > C:
			continue
		left = 0
		right = len(sub_left)
		while left < right:
			mid = (left+right) // 2
			if sub_left[mid]+i > C:
				right = mid
			else:
				left = mid+1
		answer += right

	return answer

if __name__ == "__main__":
	N,C = map(int,stdin.readline().split())
	m = list(map(int,stdin.readline().split()))
	print(solution(N,C,m))