import sys
from collections import deque

directions = [(0, 1),  # RIGHT
              (1, 0),  # DOWN
              (0, -1),  # LEFT
              (-1, 0)]  # UP


def count_adjacent_soldiers(game_map, width, height, y, x, checked_positions):
    queue = deque([(y, x)])
    checked_positions[y][x] = True
    count = 1

    while queue:
        y, x = queue.popleft()

        for y_direction, x_direction in directions:
            new_x = x + x_direction
            new_y = y + y_direction

            if 0 <= new_x < width and 0 <= new_y < height and \
                    not checked_positions[new_y][new_x] and \
                    game_map[new_y][new_x] == game_map[y][x]:
                queue.append((new_y, new_x))
                checked_positions[new_y][new_x] = True
                count += 1

    return count


def calculate_army_power(width, height, game_map):
    checked_positions = [[False] * width for _ in range(height)]

    my_army_power = 0
    enemy_army_power = 0

    for y in range(height):
        for x in range(width):
            if not checked_positions[y][x]:
                group_member = count_adjacent_soldiers(game_map, width, height, y, x, checked_positions)
                if game_map[y][x] == 'W':
                    my_army_power += group_member ** 2
                elif game_map[y][x] == 'B':
                    enemy_army_power += group_member ** 2

    return my_army_power, enemy_army_power


width, height = map(int, sys.stdin.readline().split())
game_map = []

for _ in range(height):
    game_map.append(list(sys.stdin.readline().strip()))

army_power = calculate_army_power(width, height, game_map)

print(army_power[0], army_power[1])
