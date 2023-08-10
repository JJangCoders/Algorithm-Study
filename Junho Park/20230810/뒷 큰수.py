# This is my solution for Programmers 154539
# 뒤에 있는 큰 수 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/154539

# def solution(numbers):
#     answer = []
#     length = len(numbers)
#     for i in range(length):
#         backNum = -1
#         for j in range(i+1, length):
#             if numbers[i] < numbers[j]:
#                 backNum = numbers[j]
#                 break
#         answer.append(backNum)
#     return answer

def solution(numbers):
    stack = []
    answer = [0] * len(numbers)

    for i in range(len(numbers)):
            while stack and numbers[stack[-1]] < numbers[i]:
                answer[stack.pop()] = numbers[i]
            stack.append(i)
    while stack:
            answer[stack.pop()] = -1
    
    return answer