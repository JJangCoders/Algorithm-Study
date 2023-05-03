original_length_of_side = int(input())
original_paper = []
result = [0, 0]

for _ in range(original_length_of_side):
    original_paper.append(list(map(int, input().split())))


def slice_paper(paper):
    length_of_side = len(paper)

    if is_monochrome(paper, length_of_side):  # 종이가 단색일 경우
        result[paper[0][0]] += 1
    else:  # 종이가 단색이 아닐 경우, 4등분하여 재귀적으로 확인
        slice_paper([row[:length_of_side // 2] for row in paper[:length_of_side // 2]])
        slice_paper([row[length_of_side // 2:] for row in paper[:length_of_side // 2]])
        slice_paper([row[:length_of_side // 2] for row in paper[length_of_side // 2:]])
        slice_paper([row[length_of_side // 2:] for row in paper[length_of_side // 2:]])


def is_monochrome(paper, length_of_side):  # 종이가 단색인지 확인하는 함수
    for y in range(length_of_side):
        for x in range(length_of_side):
            if paper[y][x] != paper[0][0]:
                return False

    return True


slice_paper(original_paper)

print(result[0])
print(result[1])
