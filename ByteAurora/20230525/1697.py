from collections import deque

subin_pos, brother_pos = map(int, input().split())

game_map = [0] * 100001

subin_pos_queue = deque([subin_pos])
while subin_pos_queue:  # 수빈이의 위치 목록이 비어있지 않을 때까지
    subin_pos = subin_pos_queue.popleft()  # 수빈이의 위치 하나 추출

    if subin_pos == brother_pos:  # 수빈이의 위치가 동생의 위치가 같을 경우
        print(game_map[subin_pos])  # 수빈이가 동생을 찾은 시간 출력
        break

    for subin_next_pos in [subin_pos - 1, subin_pos + 1, subin_pos * 2]:  # 수빈이의 이동할 수 있는 다음 위치 접근
        if 0 <= subin_next_pos <= 100000 and not game_map[subin_next_pos]:  # 최소, 최대 위치를 넘지 않고 아직 방문하지 않은 위치일 경우
            game_map[subin_next_pos] = game_map[subin_pos] + 1  # 해당 위치에 수빈이가 도달하는 시간을 저장
            subin_pos_queue.append(subin_next_pos)  # 해당 위치를 수빈이의 위치 목록에 추가
