from sys import stdin

n, w, L = map(int, stdin.readline().split())

weights_of_trucks = list(map(int, stdin.readline().split()))

bridge_map = []
truck_distance_remain = []
total_weight = 0    #total weight of trucks on the bridge
truck_index = 0     #pointer to the next truck crossing the bridge
#input

time = 0

while truck_index < n:
    if total_weight + weights_of_trucks[truck_index] <= L:  #there is a room for another truck on bridge
        bridge_map.append(weights_of_trucks[truck_index])   #truck starts crossing the bridge
        truck_distance_remain.append(w) #truck added to distance list
        truck_index += 1

    for i in range(len(truck_distance_remain)):
        truck_distance_remain[i] -= 1
    #each truck on the bridge goes one space

    if truck_distance_remain[0] == 0:   #truck finished crossing
        del truck_distance_remain[0]
        del bridge_map[0]
    
    total_weight = sum(bridge_map)

    time = time + 1
#all trucks left the first waiting queue

while len(truck_distance_remain) > 0:   #handling for trucks left on the bridge
    for i in range(len(truck_distance_remain)):
        truck_distance_remain[i] -= 1
    if truck_distance_remain[0] == 0:   #truck finished crossing
        del truck_distance_remain[0]
        del bridge_map[0]
    time = time + 1 

print(time + 1) #last truck needs 1 unit time to finish crossing