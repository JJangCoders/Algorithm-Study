import sys

X_DIRECTION = [0, 1, 0, -1]
Y_DIRECTION = [-1, 0, 1, 0]


class Robot:
    def __init__(self, x_pos, y_pos, direction, room_data):
        self.x = x_pos
        self.y = y_pos
        self.direction = direction
        self.room_data = room_data
        self.is_active = False
        self.clean_count = 0

    def start_cleaning(self):
        self.is_active = True
        self.clean_count = 0
        while self.is_active:
            if self.room_data[self.y][self.x] == 0:  # 현재 위치가 청소되어있지 않은 경우
                self.room_data[self.y][self.x] = 2
                self.clean_count += 1

            if self.room_data[self.y][self.x - 1] == 0 \
                    or self.room_data[self.y][self.x + 1] == 0 \
                    or self.room_data[self.y - 1][self.x] == 0 \
                    or self.room_data[self.y + 1][self.x] == 0:  # 상하좌우 중 한 곳이라도 청소가 되어있지 않은 경우

                while True:
                    self.direction = (self.direction - 1) if self.direction > 0 else 3

                    if self.room_data[self.y + Y_DIRECTION[self.direction]][self.x + X_DIRECTION[self.direction]] == 0:  # 청소할 곳을 찾은 경우
                        break
            else:  # 상하좌우에 청소할 곳이 없는 경우
                if self.room_data[self.y - Y_DIRECTION[self.direction]][self.x - X_DIRECTION[self.direction]] == 1:  # 후진할 곳이 벽일 경우
                    self.is_active = False
                else:  # 후진할 곳이 벽이 아닐 경우
                    self.y -= Y_DIRECTION[self.direction]
                    self.x -= X_DIRECTION[self.direction]


room_height, room_width = map(int, sys.stdin.readline().strip().split(" "))
robot_y, robot_x, robot_direction = map(int, sys.stdin.readline().strip().split(" "))

target_room_data = [list(map(int, sys.stdin.readline().strip().split(" "))) for _ in range(0, room_height)]

robot = Robot(robot_x, robot_y, robot_direction, target_room_data)

robot.start_cleaning()

print(robot.clean_count)
