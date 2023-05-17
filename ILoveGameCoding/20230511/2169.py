import sys


def print2D(dp):
    for i in range(len(dp)):
        print(dp[i])
    print()


def find_max_total_value(cols, rows, mars_map):
    # 첫 번째 행 설정
    for row in range(1, rows):
        mars_map[0][row] = mars_map[0][row - 1] + mars_map[0][row]

    # 행별로 최대값 계산
    for col in range(1, cols):
        # 왼쪽에서부터 이동할 경우 최댓값 탐색
        start_from_left = mars_map[col][:]
        start_from_left[0] += mars_map[col - 1][0]
        for row in range(1, rows):
            start_from_left[row] += max(mars_map[col - 1][row], start_from_left[row - 1])

        # 오른쪽에서부터 이동할 경우 최댓값 탐색
        start_from_right = mars_map[col][:]
        start_from_right[rows - 1] += mars_map[col - 1][rows - 1]
        for row in range(rows - 2, -1, -1):
            start_from_right[row] += max(mars_map[col-1][row], start_from_right[row + 1])

        # 각 위치마다 방향에 따른 최댓값 결정
        for row in range(rows):
            mars_map[col][row] = max(start_from_left[row], start_from_right[row])

    return mars_map[cols - 1][rows - 1]


in_cols, in_rows = map(int, sys.stdin.readline().split())
in_mars_map = []
for col in range(in_cols):
    in_mars_map.append(list(map(int, sys.stdin.readline().split())))

print(find_max_total_value(in_cols, in_rows, in_mars_map))
