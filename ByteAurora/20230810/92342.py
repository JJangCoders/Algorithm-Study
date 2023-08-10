score_board_size = 10


def get_ryan_hit_combinations(arrow_count, length=score_board_size + 1):
    if length == 1:
        return [[arrow_count]]

    ryan_hit_combinations = []

    for i in range(arrow_count + 1):
        for combination in get_ryan_hit_combinations(arrow_count - i, length - 1):
            ryan_hit_combinations.append([i] + combination)

    return ryan_hit_combinations


def check_ryan_win(apeach_target_hits, ryan_target_hits):
    apeach_score = 0
    ryan_score = 0

    for idx in range(0, score_board_size + 1):
        score = score_board_size - idx
        if apeach_target_hits[score] == 0 and ryan_target_hits[score] == 0:
            continue
        elif apeach_target_hits[score] >= ryan_target_hits[score]:
            apeach_score += (score_board_size - score)
        elif apeach_target_hits[score] < ryan_target_hits[score]:
            ryan_score += (score_board_size - score)

    return ryan_score - apeach_score


def solution(n, info):
    answer = [-1]
    best_score_diff = -1

    for ryan_target_hits in get_ryan_hit_combinations(n):
        score_diff = check_ryan_win(info, ryan_target_hits)

        if score_diff > 0:
            if score_diff > best_score_diff:
                answer = ryan_target_hits
                best_score_diff = score_diff
            elif score_diff == best_score_diff:
                if ''.join(map(str, answer)) > ''.join(map(str, ryan_target_hits)):
                    answer = ryan_target_hits

    return answer


print(solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))
