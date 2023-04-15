# 처음에 이진 탐색 방법으로 lower_bound, upper_bound를 사용해서 풀려고 했으나, 시간 초과로 실패
# 3시간 가량 고민하다가, 더 이상 고민하면 중간고사 조질 것 같아서, 구글 검색했습니다. (_ _)
# 투 포인터로, 오른쪽 끝, 왼쪽 끝 인덱스를 조절해주면서 값을 찾아나가는 방식으로 구현했습니다.

from sys import stdin

N = int(stdin.readline())

numbers = list(map(int, stdin.readline().split()))

sorted_numbers = sorted(numbers)

good_count = 0
#init

for i in range(N):
    numbers_without_i = sorted_numbers[:i] + sorted_numbers[i+1:]
    left, right = 0, len(numbers_without_i) - 1

    while left < right:
        left_plus_right = numbers_without_i[left] + numbers_without_i[right]

        if left_plus_right == sorted_numbers[i]:
            good_count += 1
            break

        if left_plus_right > sorted_numbers[i]:
            right -= 1
        else:
            left += 1
print(good_count)