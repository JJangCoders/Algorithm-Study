import sys


# 아래는 가독성을 위해 배열을 비교하는 함수를 별도로 만든 것이고, 이렇게 함수를 만들어서 호출하는 것보다
# for문을 직접 일일히 작성하는 방식이 약 180ms 더 빠름
def compare_arrays(start, end):  # 배열을 인덱스를 기준으로 비교하는 함수
    for idx in range(start, end):
        if original_arr[idx] != target_arr[idx]:
            return False
    return True


arr_size, original_arr, target_arr = int(input()), list(map(int, sys.stdin.readline().split())), list(
    map(int, sys.stdin.readline().split()))

if original_arr == target_arr:
    print(1)
else:
    # 버블정렬
    for sorted_count in range(arr_size - 1):
        swapped = False  # 이번 순환에서 변경 발생 여부

        need_to_compare = True  # 이번 순환에서 변경이 발생했을 경우, 타겟 배열과 비교하는지 검사하는 과정이 필요한지에 대한 여부
        for comp_idx in range(arr_size - 1 - sorted_count):
            if original_arr[comp_idx] > original_arr[comp_idx + 1]:
                original_arr[comp_idx], original_arr[comp_idx + 1] = original_arr[comp_idx + 1], original_arr[comp_idx]
                swapped = True

                if need_to_compare:
                    if compare_arrays(0, arr_size - 1 - sorted_count):
                        # 이미 정렬되어 값이 고정된 부분을 제외한 나머지 부분이 타겟 배열과 일치할 경우
                        print(1)
                        exit()

                    if not compare_arrays(0, comp_idx + 1):
                        # 이번 비교가 일어난 지점까지의 배열이 타겟 배열과 일치하지 않을 경우
                        # 다음 새로운 순환이 되기 전 까지는 더 이상 일치할 일이 없음
                        need_to_compare = False

        if not compare_arrays(arr_size - 1 - sorted_count, arr_size):
            # 이번 순환에서 변경이 완료 되었을 때, 이미 정렬이 완료된 부분이 타겟 배열과 일치하지 않을 경우
            # 해당 배열은 더 이상 타겟 배열과 일치할 수 있는 경우가 없음
            print(0)
            break

        if not swapped:  # 순환 도중 변경이 단 한번도 일어나지 않았다면 정렬 완료
            if original_arr == target_arr:
                print(1)
            else:
                print(0)
            break
