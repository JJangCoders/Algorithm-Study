from sys import stdin
import heapq

# My first attempt -> timeout
# n = int(stdin.readline())

# heap = []

# for i in range(n):
#     size_of_heap = len(heap)
#     insert_index = 0

#     number_input = int(stdin.readline())

#     if number_input == 0:
#         if size_of_heap == 0:
#             print(0)
#         else:
#             print(heap[0])
#             del heap[0]
#     else:
#         abs_number_input = abs(number_input)
#         if size_of_heap > 0:
#             prev_number = abs(heap[0])
#         for insert_index in range(size_of_heap):
#             abs_heap_number = abs(heap[insert_index])
#             if prev_number == abs_heap_number:
#                 if insert_index == size_of_heap - 1:
#                     insert_index += 1
#                 continue
#             if abs_heap_number < abs_number_input:
#                 insert_index += 1
#                 break
#             elif abs_heap_number == abs_number_input:
#                 if number_input < 0:
#                     insert_index -= 1
#                     break
#             prev_number = abs_heap_number
#         print('insert index: ', insert_index)

#         if insert_index == 0:
#             heap = [number_input] + heap[:]
#         else:
#             heap = heap[:insert_index + 1] + [number_input] + heap[insert_index+1:]

#     print(heap)

n = int(stdin.readline())

heap = []

for i in range(n):
    number = int(stdin.readline())
    if number == 0:
        if len(heap) == 0:
            print(0)
        else:
            _, first_number = heapq.heappop(heap)
            print(first_number)
    else:
        heapq.heappush(heap, (abs(number), number))