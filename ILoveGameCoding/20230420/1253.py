numbers_count = int(input())
numbers = list(map(int, input().split(' ')))
idx = -1
low_idx = 0
high_idx = 0
good_numbers = 0
length = len(numbers)

numbers.sort()  # numbers를 오름차순으로 정렬

for idx in range(0, length):
    low_idx = 0
    high_idx = length - 1

    while low_idx < high_idx:  # 낮은 값의 인덱스가 높은 값의 인덱스보다 작을 때까지 반복
        if low_idx == idx: # 낮은 값의 인덱스가 현재 인덱스와 같을 경우 1을 더해줌
            low_idx += 1
            continue
        if high_idx == idx: # 높은 값의 인덱스가 현재 인덱스와 같을 경우 1을 뺴줌
            high_idx -= 1
            continue

        if numbers[low_idx] + numbers[high_idx] == numbers[idx]:
            # 합이 현재 인덱스에 해당되는 numbers의 값과 같을 경우
            good_numbers += 1
            break
        elif numbers[low_idx] + numbers[high_idx] > numbers[idx]:
            # 합이 현재 인덱스에 해당되는 numbers의 값보다 클 경우 높은 값 인덱스를 감소
            high_idx -= 1
        else:
            # 합이 현재 인덱스에 해당되는 numbers의 값보다 작을 경우 낮은 값 인덱스를 증가
            low_idx += 1

print(good_numbers)
