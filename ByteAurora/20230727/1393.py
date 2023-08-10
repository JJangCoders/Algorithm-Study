import math
import sys

def get_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def find_best_position(terminal_x, terminal_y, train_x, train_y, train_x_speed, train_y_speed):
    gcd = math.gcd(train_x_speed, train_y_speed)
    train_x_speed = train_x_speed // gcd
    train_y_speed = train_y_speed // gcd
    min_distance = get_distance((train_x, train_y), (terminal_x, terminal_y))

    while True:
        new_distance = get_distance((train_x, train_y), (terminal_x, terminal_y))

        if new_distance > min_distance:
            return train_x - train_x_speed, train_y - train_y_speed
        else:
            min_distance = new_distance

        train_x += train_x_speed
        train_y += train_y_speed

terminal_x, terminal_y = map(int, sys.stdin.readline().strip().split())
train_x, train_y, train_x_speed, train_y_speed = map(int, sys.stdin.readline().strip().split())

result = find_best_position(terminal_x, terminal_y, train_x, train_y, train_x_speed, train_y_speed)
print(result[0], result[1])
