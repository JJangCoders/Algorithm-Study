import sys
from collections import deque

node_count = int(input())
node_connections = [[] for _ in range(node_count + 1)]
node_parents = [0] * (node_count + 1)

for _ in range(node_count - 1):
    node_1, node_2 = map(int, sys.stdin.readline().split())
    node_connections[node_1].append(node_2)
    node_connections[node_2].append(node_1)

node_queue = deque([1])  # queue에 1번 노드 추가
while node_queue:  # queue가 비어있지 않을 때까지
    node = node_queue.popleft()  # queue에서 노드 하나 추출

    for next_node in node_connections[node]:  # 해당 노드와 연결된 노드들을 접근
        if not node_parents[next_node]:  # 아직 부모 노드가 없는 경우
            node_parents[next_node] = node  # 해당 노드의 부모 노드를 현재 노드로 설정
            node_queue.append(next_node)  # 해당 노드를 queue에 추가

for idx in range(2, node_count + 1):
    print(node_parents[idx])
