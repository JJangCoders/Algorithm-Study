import sys
T = int(sys.stdin.readline())
box_size = list(map(int,sys.stdin.readline().split()))
box_count = [0] * len(box_size)

box_count[0] = 1
for i in range(1,len(box_size)):
    size_max = -1
    for j in range(0,i):
        if box_size[i] <= box_size[j]:
            pass
        else:
            if size_max < box_count[j]:
                size_max = box_count[j]
    if size_max == -1:
        box_count[i] = 1
    else:
        box_count[i] = size_max + 1
print(box_count)
print(max(box_count))