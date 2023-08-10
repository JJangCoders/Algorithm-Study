# 아래는 처음 풀었던 방법
# def find_nearest_big_number(numbers):
#     for number in numbers[1:]:
#         if numbers[0] < number:
#             return number
#
#     return -1
#
#
# def solution(numbers):
#     answer = []
#
#     for idx in range(len(numbers)):
#         answer.append(find_nearest_big_number(numbers[idx:]))
#
#     return answer

# 스택을 이용하여 푼 방법
def solution(numbers):
    answer = [-1 for _ in range(len(numbers))]
    stack = []

    for idx, number in enumerate(numbers):
        while stack and number > numbers[stack[-1]]:  # 스택이 비어있지 않고, 현재 숫자가 스택의 마지막 숫자보다 큰 경우
            answer[stack.pop()] = number

        stack.append(idx)

    return answer
