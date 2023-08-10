from bisect import bisect_right


def get_possible_cases(weights):
    cases = [0]
    for i in weights:
        for j in range(len(cases)):
            cases.append(cases[j] + i)
    return cases


def get_possible_grouping_count(item_count, bag_size, weights):
    weight_group1 = weights[:item_count // 2]
    weight_group2 = weights[item_count // 2:]

    group1_cases = get_possible_cases(weight_group1)
    group2_cases = get_possible_cases(weight_group2)

    group2_cases.sort()

    result = 0
    for group1_case in group1_cases:
        if bag_size - group1_case >= 0:
            result += bisect_right(group2_cases, bag_size - group1_case)

    return result


N, C = map(int, input().split())
weights = list(map(int, input().split()))

print(get_possible_grouping_count(N, C, weights))
