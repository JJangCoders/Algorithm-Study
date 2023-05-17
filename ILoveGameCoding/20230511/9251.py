str1 = input()
str2 = input()


dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

for str1_idx in range(1, len(str1) + 1): # 첫 번째 문자열 탐색 인덱스
    for str2_idx in range(1, len(str2) + 1): # 두 번째 문자열 탐색 인덱스
        if str1[str1_idx - 1] == str2[str2_idx - 1]:
            # -1을 해주는 이유는 연산 편리성을 위해 dp를 1씩 증가시켜 생성했기 때문
            # 첫 번째 문자열의 인덱스와 두 번째 문자열의 인덱스가 같을 경우
            # 이전 문자열의 최대 공통 부분 수열에 +1 => 최대 공통 부분 수열 길이 1 증가
            dp[str1_idx][str2_idx] = dp[str1_idx - 1][str2_idx - 1] + 1
        else:
            # 첫 번째 문자열의 인덱스와 두 번째 문자열의 인덱스가 다를 경우
            # 이전 문자열의 최대 공통 부분 수열 중 최대 길이를 가져옴
            dp[str1_idx][str2_idx] = max([dp[str1_idx - 1][str2_idx], dp[str1_idx][str2_idx - 1]])

print(dp[len(str1)][len(str2)])
