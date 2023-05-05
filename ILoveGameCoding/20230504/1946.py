import sys

testcase_count = int(input())

for _ in range(testcase_count):
    people_count = int(input())
    candidate_ranks = []

    for _ in range(people_count):
        candidate_ranks.append(list(map(int, sys.stdin.readline().split())))

    # 서류심사 성적으로 정렬
    candidate_ranks.sort(key=lambda x: x[0])

    hiring_count = 0

    # 현재까지 확인한 지원자 중 가장 높은 면접 순위
    max_interview_rank = candidate_ranks[0][1]
    for _, interview_rank in candidate_ranks:
        if interview_rank <= max_interview_rank:
            # 현재 지원자의 면접 순위가 지금까지 확인한 지원자 중
            # 가장 높은 면접 순위보다 높을 경우(숫자상으로는 작을 경우)
            hiring_count += 1
            max_interview_rank = interview_rank

    print(hiring_count)
