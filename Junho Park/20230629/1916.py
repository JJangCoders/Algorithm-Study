from sys import stdin
import heapq

def dijkstra(start):

    # start = a city number

    # init
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for node in graph[now]:
            cost = dist + node[1]
            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(q, (cost, node[0]))

# an integer variable that is larger than anything in this program
INF = float("inf")

# number of cities
N = int(stdin.readline())

# number of buses
M = int(stdin.readline())

# distances
distance = [INF] * (N+1)

# graph
# graph[a] = (b, c) means the cost of traveling from a to b is c.
graph = [[] for i in range(N+1)]

# graph input
for _ in range(M):
    a,b,c = map(int, stdin.readline().split())
    graph[a].append((b,c))

# departure and destination
start, end = map(int, stdin.readline().split())

# running the Dijkstra Algorithm
dijkstra(start)

# printing minimum distance
print(distance[end])