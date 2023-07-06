import sys

number_of_days, withdrawal_count = map(int, sys.stdin.readline().split()) # 날짜 수, 인출 횟수
cost_of_days = [int(sys.stdin.readline()) for _ in range(number_of_days)] # 각 날짜별 사용할 금액 목록

'''
1. 인출 금액 k의 최소값, 최대값 지정
2. 최소값과 최대값의 중간값을 구함
3. 중간값으로 인출했을 경우의 인출 횟수 추출
    3-1. 인출 횟수가 withdrawal_count보다 작으면 최소값을 중간값으로 변경
    3-2. 인출 횟수가 withdrawal_count보다 크면 최대값을 중간값으로 변경
4. 최소값 인출 금액이 최대 인출 금액보다 작을 때까지 3번 과정 반복
'''
min_withdrawal = max(cost_of_days)
max_withdrawal = sum(cost_of_days)

while min_withdrawal <= max_withdrawal:
    mid_withdrawal = (min_withdrawal + max_withdrawal) // 2
    mid_withdrawal_count = 1
    mid_withdrawal_sum = 0

    for cost in cost_of_days:
        if mid_withdrawal_sum + cost > mid_withdrawal:
            mid_withdrawal_sum = 0
            mid_withdrawal_count += 1
        mid_withdrawal_sum += cost

    if mid_withdrawal_count <= withdrawal_count:
        max_withdrawal = mid_withdrawal - 1
    else:
        min_withdrawal = mid_withdrawal + 1

print(min_withdrawal)
