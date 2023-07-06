import sys
from collections import deque

for _ in range(int(input())):
    # 건물 개수 및 건설 순서 규칙 개수 입력
    building_count, construction_sequence_count = map(int, sys.stdin.readline().split())

    # 건물 건설 시간 입력
    build_time = [0] + list(map(int, input().split()))

    # 건설 순서
    build_dependency = [[] for _ in range(building_count + 1)]
    # 각 건물을 건설하기 위해 선행적으로 건설되어야 하는 건물의 개수
    dependency_count = [0] * (building_count + 1)

    # 건설 순서 규칙 입력
    for _ in range(construction_sequence_count):
        parent, child = map(int, sys.stdin.readline().split())
        build_dependency[parent].append(child)
        dependency_count[child] += 1

    # 최종적으로 건설해야 하는 건물 입력
    last_building = int(input())

    # 각 건물을 건설하는데 필요한 최소 시간
    min_build_time = [0] * (building_count + 1)

    # 선행 건물이 없는 건물들을 저장
    starts = deque()

    # 선행 건물들을 초기화
    for building in range(1, building_count + 1):
        if dependency_count[building] == 0:
            starts.append(building)
            min_build_time[building] = build_time[building]

    # 선행 건물이 없는 건물들부터 시작 => 각 건물을 짓는데 필요한 최소 시간 계산
    while starts:
        current_building = starts.popleft()

        # 현재 건물이 선행 건물인 건물들에 대해 해당 건물들을 짓는데 필요한 최소 시간을 계산
        for next_building in build_dependency[current_building]:
            dependency_count[next_building] -= 1
            min_build_time[next_building] = max(min_build_time[next_building],
                                                min_build_time[current_building] + build_time[next_building])

            if dependency_count[next_building] == 0:  # 현재 건물을 건설하기 위한 선행 건물들이 모두 건설되었을 경우
                starts.append(next_building)

        if dependency_count[last_building] == 0:  # 최종적으로 건설해야 하는 건물의 선행 건물들이 모두 건설되었을 경우
            print(min_build_time[last_building])
            break
