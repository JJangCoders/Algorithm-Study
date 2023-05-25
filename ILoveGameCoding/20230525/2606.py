def check_infected_computer(computer_connections, start_computer, checked_computers):
    checked_computers[start_computer] = True  # 현재 컴퓨터를 확인된 컴퓨터로 표시

    for connected_computer in computer_connections[start_computer]:  # 연결된 컴퓨터들을 확인
        if not checked_computers[connected_computer]:  # 아직 확인되지 않은 컴퓨터일 경우
            check_infected_computer(computer_connections, connected_computer, checked_computers)


computer_count = int(input())
connection_count = int(input())

computer_connections = [[] for _ in range(computer_count + 1)]

for _ in range(connection_count):
    computer_1, computer_2 = map(int, input().split())
    computer_connections[computer_1].append(computer_2)
    computer_connections[computer_2].append(computer_1)

# 연산 편리성을 위해 0번 인덱스는 사용하지 않고 1번부터 사용
checked_computers = [False] * (computer_count + 1)

check_infected_computer(computer_connections, 1, checked_computers)

print(checked_computers.count(True) - 1)
