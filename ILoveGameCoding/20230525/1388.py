height, width = map(int, input().split())

floor_map = []

for _ in range(height):
    floor_map.append([char for char in input()])

tile_count = 0

for h_idx in range(height):
    for w_idx in range(width):
        if floor_map[h_idx][w_idx] == -1:
            continue

        tile_count += 1
        if floor_map[h_idx][w_idx] == '-':
            temp_w_idx = w_idx
            while temp_w_idx < width and floor_map[h_idx][temp_w_idx] == '-':
                floor_map[h_idx][temp_w_idx] = -1
                temp_w_idx += 1
        elif floor_map[h_idx][w_idx] == '|':
            temp_h_idx = h_idx
            while temp_h_idx < height and floor_map[temp_h_idx][w_idx] == '|':
                floor_map[temp_h_idx][w_idx] = -1
                temp_h_idx += 1

print(tile_count)
