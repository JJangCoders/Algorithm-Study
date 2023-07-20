import sys
from collections import deque


def solution(original_string):
    string_length = len(original_string)
    converted_string = ""
    temp_string = deque()
    idx = 0

    while idx < string_length:
        if original_string[idx] == "<":
            while original_string[idx] != ">":
                converted_string += original_string[idx]
                idx += 1
            converted_string += original_string[idx]
            idx += 1
        elif original_string[idx] == " ":
            converted_string += " "
            idx += 1
        else:
            while idx < string_length and original_string[idx] != " " and original_string[idx] != "<":
                temp_string.appendleft(original_string[idx])
                idx += 1
            converted_string += "".join(temp_string)
            temp_string.clear()

    return converted_string


S = sys.stdin.readline().strip()

print(solution(S))
