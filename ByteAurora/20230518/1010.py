testcase_count = int(input())


for _ in range(testcase_count):
    left_side, right_side = list(map(int, input().split()))

    # 2차원 dp 사용
    # dp = [[0 for _ in range(right_side + 1)] for _ in range(left_side + 1)]
    # 
    # # left_side, right_side가 동일한 부분을 1로 채움
    # for left_idx in range(1, left_side + 1):
    #     dp[left_idx][left_idx] = 1
    # 
    # # left_side가 1인 부분들은 right_idx 값으로 각각 채움
    # # 해당 부분은 좌측 다리 포인트가 1이므로 우측 다리 포인트 개수에 따라
    # # 다리를 놓을 수 있는 경우의 수가 주어짐
    # for right_idx in range(right_side + 1):
    #     dp[1][right_idx] = right_idx
    # 
    # for left_idx in range(2, left_side + 1):  # left_idx를 2 이상인 부분 계산 시작
    #     for right_idx in range(left_idx + 1, right_side + 1):
    #         # right_idx는 left_idx보다 1 큰 위치부터 시작
    #         # 왜냐하면, left_idx, right_idx가 동일한 위치는 이미 1로
    #         # 채워져 있기 때문에 수정할 필요가 없음
    #         
    #         # 다리 포인트가 좌측은 left_idx개, 우측은 right_idx개인 경우 놓을 수 있는 다리의 수는
    #         # 좌측 다리 포인트가 1 작을 때, 우측 다리 포인트가 1부터 right_idx인 경우의 수의 합과 동일
    #         dp[left_idx][right_idx] = sum([dp[left_idx - 1][val] for val in range(1, right_idx)])
    # 
    # print(dp[left_side][right_side])

    # 1차원 dp 이용
    # m! / (n! * (m-n)!)
    dp = [0] * (right_side + 1)
    dp[0] = 1

    for right_idx in range(1, right_side + 1):
        for left_idx in range(min(right_idx, left_side), 0, -1):
            dp[left_idx] += dp[left_idx - 1]

    print(dp[left_side])
