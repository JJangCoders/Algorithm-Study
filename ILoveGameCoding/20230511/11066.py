import sys


# 문제를 해결하기 위한 방법은, 특정 구간에 해당되는 파일들을
# 합쳤을 때의 최소 비용을 구하고 이를 이용하여 전체 파일을
# 합칠 때의 최소 비용을 구하는 것
def min_cost_to_merge_files_dp(file_count, file_sizes):
    # 특정 구간을 표현하기 위해 start_idx, end_idx가 필요하며, 이를 위해
    # 2차원 배열로 구현
    dp = [[0 for _ in range(file_count)] for _ in range(file_count)]
    sums = [0 for _ in range(file_count)]
    sums[0] = file_sizes[0]

    # 시작 구간부터 특정 구간까지의 파일들의 총합 저장
    for i in range(1, file_count):
        sums[i] = sums[i - 1] + file_sizes[i]

    # 연속된 2개의 파일을 묶은 값의 합 저장
    # for start_idx in range(file_count - 1):
    #     dp[start_idx][start_idx + 1] = file_sizes[start_idx] + file_sizes[start_idx + 1]

    # 각 파일들을 한번에 묶을 수 있는 개수 (2부터 최대 파일 개수까지)
    for group_size in range(2, file_count + 1):
        # 시작 구간부터 그룹 사이즈만큼 그룹핑
        for start_idx in range(file_count - group_size + 1):
            # 그룹의 마지막 인덱스
            end_idx = start_idx + group_size - 1

            # 그룹의 시작 인덱스부터 그룹의 마지막 인덱스까지의 최소 병합 비용
            # 내부 for문은 각 구간을 나눌 수 있는 모든 경우로 나누고 그 구간별 합의 최소 비용을 구함
            # 그렇게 도출된 최소 비용에 그룹핑 구간의 전체 파일의 총합을 더해서
            # 그룹핑 구간의 최소 병합 비용을 구함
            dp[start_idx][end_idx] = min(
                [dp[start_idx][start_idx + length] + dp[start_idx + length + 1][end_idx] for length in
                 range(end_idx - start_idx)]) + (sums[end_idx] - (sums[start_idx - 1] if start_idx > 0 else 0))

    return dp[0][file_count - 1]


for _ in range(int(input())):
    in_file_count = int(input())
    in_file_sizes = list(map(int, sys.stdin.readline().split()))

    print(min_cost_to_merge_files_dp(in_file_count, in_file_sizes))
