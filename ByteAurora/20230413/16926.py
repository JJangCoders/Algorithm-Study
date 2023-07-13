import sys


def get_rotate_point(depth, max_x, max_y, org_x, org_y, rotate_cnt):
    temp_width = max_x + 1 - depth * 2
    temp_height = max_y + 1 - depth * 2
    outside_count = ((temp_width * temp_height) - (temp_width - 2) * (temp_height - 2))
    in_rotate_count = rotate_cnt % outside_count
    mode = 0 if in_rotate_count <= outside_count / 2 else 1

    if mode == 0:
        for _ in range(0, in_rotate_count):
            if org_x == depth and max_y - depth != org_y:
                org_y += 1
                continue
            if org_y == max_y - depth and max_x - depth != org_x:
                org_x += 1
                continue
            if org_x == max_x - depth and org_y != depth:
                org_y -= 1
                continue
            if org_y == depth and org_x != depth:
                org_x -= 1
                continue
    else:
        for _ in range(0, outside_count - in_rotate_count):
            if org_x == depth and org_y != depth:
                org_y -= 1
                continue
            if org_y == max_y - depth and org_x != depth:
                org_x -= 1
                continue
            if org_x == max_x - depth and org_y != max_y - depth:
                org_y += 1
                continue
            if org_y == depth and org_x != max_x - depth:
                org_x += 1
                continue

    return org_x, org_y


height, width, rotate_count = [int(x) for x in sys.stdin.readline().split(" ")]

original_map = []

for _ in range(0, height):
    original_map.append(sys.stdin.readline().strip().split(" "))

result_map = [[0 for _ in range(0, width)] for _ in range(0, height)]

for y in range(0, height):
    for x in range(0, width):
        new_x, new_y = get_rotate_point(min(x, y, width - 1 - x, height - 1 - y), width - 1, height - 1, x, y,
                                        rotate_count)
        result_map[new_y][new_x] = original_map[y][x]

for y in range(0, height):
    for x in range(0, width):
        print(result_map[y][x], end=" ")
    if y != height - 1:
        print()
