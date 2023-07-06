import sys

base_pattern = ['***', '* *', '***']  # 기본 패턴


def solution(size):
    if size == 3:  # 최소 사이즈일 경우 기본 패턴 반환
        return base_pattern
    else:
        low_level_pattern_size = size // 3  # 한 단계 낮은 패턴의 사이즈
        low_level_pattern = solution(low_level_pattern_size)  # 한 단계 낮은 패턴

        # 패턴을 크게 가로를 기준으로 나눴을 때 상, 중, 하 중에서 중에 해당되는 영역
        middle = [low_level_pattern_row + ' ' * low_level_pattern_size + low_level_pattern_row for low_level_pattern_row
                  in low_level_pattern]

        # 상, 중, 하를 합쳐서 반환
        return [low_level_pattern_row * 3 for low_level_pattern_row in low_level_pattern] + middle + [
            low_level_pattern_row * 3 for
            low_level_pattern_row in low_level_pattern]


N = int(sys.stdin.readline())
print('\n'.join(solution(N)))
