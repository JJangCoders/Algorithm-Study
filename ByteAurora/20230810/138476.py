def solution(k, tangerine):
    answer = 0
    mandarins = {}

    for size in tangerine:
        if size in mandarins:
            mandarins[size] += 1
        else:
            mandarins[size] = 1

    selected_count = 0

    for size, count in sorted(mandarins.items(), key=lambda x: x[1], reverse=True):
        selected_count += count
        answer += 1

        if selected_count >= k:
            break

    return answer
