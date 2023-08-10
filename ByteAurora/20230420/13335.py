class BridgeManager:
    def __init__(self, bridge_length, bridge_weight_limit):
        self.bridge_length = bridge_length
        self.bridge_weight_limit = bridge_weight_limit
        self.wait_list = []
        self.trucks_on_bridge = [0] * bridge_length
        self.current_bridge_weight = 0
        self.working_time = 0

    def set_wait_list(self, waiting_trucks):
        self.wait_list = waiting_trucks

    def begin_entrance(self):
        while True:  # 차량 출입 시작
            self.current_bridge_weight -= self.trucks_on_bridge.pop(0)

            if len(self.wait_list) > 0:
                if self.current_bridge_weight + self.wait_list[0] > self.bridge_weight_limit:
                    # 대기 중인 첫 번째 트럭이 들어오면 다리의 최대 하중을 넘어서는 경우
                    self.trucks_on_bridge.append(0)
                else:
                    # 대기 중인 첫 번째 트력이 들어와도 다리의 최대 하중을 넘지 않는 경우
                    self.current_bridge_weight += self.wait_list[0]
                    self.trucks_on_bridge.append(self.wait_list.pop(0))
            else:
                self.trucks_on_bridge.append(0)

            self.working_time += 1

            if self.current_bridge_weight == 0:  # 모든 트럭이 다리를 건넜을 경우 종료
                break


in_trucks_count, in_bridge_length, in_bridge_weight_limit = map(int, input().split(' '))
in_waiting_trucks = list(map(int, input().split(' ')))

bridge_manager = BridgeManager(in_bridge_length, in_bridge_weight_limit)
bridge_manager.set_wait_list(in_waiting_trucks)
bridge_manager.begin_entrance()

print(bridge_manager.working_time)
