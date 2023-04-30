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

#여기서부턴 제가 원래 이진탐색 방법으로 풀려했던 코드입니다.
# from sys import stdin

# N = int(stdin.readline())
# numbers = list(map(int, stdin.readline().split()))
# sorted_numbers = sorted(numbers)
# #input and sorting

# smallest_number = sorted_numbers[0]
# second_smallest_number = sorted_numbers[1]
# good_count = 0
# good_number_found_flag = False
# #init values

# for number in sorted_numbers:
#     if number < smallest_number + second_smallest_number:
#         continue
    
#     good_number_found_flag = False
#     upper_cap = N//2

#     if number <= sorted_numbers[upper_cap]:
#         while number <= sorted_numbers[upper_cap]:
#             upper_cap = upper_cap//2
#         if number > sorted_numbers[upper_cap]:
#             upper_cap *= 2
#     else:
#         while number > sorted_numbers[upper_cap]:
#             upper_cap = upper_cap + (N - upper_cap)//2
#     #taking care of the upper bound

#     lower_cap = 0
#     exp = 0

#     while sorted_numbers[lower_cap] + sorted_numbers[upper_cap] < number:
#         lower_cap = 2**exp
#         exp += 1
#     lower_cap = lower_cap // 2
    
#     for i in range(upper_cap + 1):
#         for j in range(i + 1, upper_cap + 1):
#             result = sorted_numbers[i] + sorted_numbers[j]
#             if result == number:
#                 good_count += 1
#                 good_number_found_flag = True
#                 break
#             elif result > number:
#                 break
#         if good_number_found_flag:
#             break

# print(good_count)