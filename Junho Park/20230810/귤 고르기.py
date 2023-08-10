# This is my solution for Programmers 138476
# 귤 고르기
# https://school.programmers.co.kr/learn/courses/30/lessons/138476

# initial approach --> timeout

# from itertools import combinations
# def calcDiff(tangerine):
#     idx = {}
#     for t in tangerine:
#         idx[t] = 1
#     return len(idx)

# def solution(k, tangerine):
#     minDiff = k
    
#     for set in combinations(tangerine, k):
#         diff = calcDiff(set)
#         if diff < minDiff:
#             minDiff = diff
            
#     return minDiff

# second approach --> timeout

# from itertools import combinations

# def solution(k, tangerine):
#     minDiff = k
    
#     for comb in combinations(tangerine, k):
#         diff = len(set(comb))
#         if diff < minDiff:
#             minDiff = diff
            
#     return minDiff

def solution(k, tangerine):
    answer = 0
    check = 0
    tangerine.sort()
    dup = {}
    for i in tangerine:
        if i in dup:
            dup[i] += 1
        else:
            dup[i] = 1

    arr = sorted(dup.items(), key=lambda x: x[1], reverse=True)
    if arr[0][1] >= k:
        return 1
    else:
        for i in arr:
            if check < k:
                check += i[1]
                answer += 1
            else:
                break
    return answer