# this is my solution for BaekJoon 12015
# 가장 긴 증가하는 부분 수열 2
# https://www.acmicpc.net/problem/12015
# =======================================
# References
# https://jainn.tistory.com/92
# https://jainn.tistory.com/90

from sys import stdin

N = int(stdin.readline())
sequence = list(map(int, stdin.readline().split()))
arr = [0]

for n in sequence:
    if arr[-1] < n:
        arr.append(n)
    else:
        left = 0
        right = len(arr)
        while left < right:
            mid = (left + right)//2
            if arr[mid] < n:
                left = mid + 1
            else:
                right = mid
        arr[right] = n

print(len(arr) - 1)