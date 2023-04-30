# 반례
# 4 3
# 1 1
# 2 1 2
# 2 2 3
# 2 3 4
# import sys
# N,P = map(int,sys.stdin.readline().split())
# how_many = list(map(int,sys.stdin.readline().split()))
# answer = 0
# new_how_many = []
# re_confirm = []
# if how_many[0] == 0:
#     print(P)
# else:
#     for party in range(P):
#         not_gwa = 0
#         in_party = list(map(int,sys.stdin.readline().split()))
#         for person in in_party[1:]:
#             if person in how_many[1:]:
#                 not_gwa = 1
#                 break
#         if not not_gwa:
#             answer += 1
#             re_confirm.append(in_party[1:])
#         else:
#             new_how_many.extend(in_party[1:])
#     new_how_many = set(new_how_many)
#     for party in re_confirm:
#         for people in party:
#             if people in new_how_many:
#                 answer -= 1
#                 break
#     print(answer)

import sys
N,P = map(int,sys.stdin.readline().split())
how_many = list(map(int,sys.stdin.readline().split()))
parties = []
for case in range(P):
    parties.append(list(map(int,sys.stdin.readline().split()))[1:])
if how_many[0] == 0:
    print(P)
else:
    how_many = how_many[1:]
    for case in range(P):
        for party in parties:
            flag = 0
            for member in party:
                if member in how_many:
                    flag = 1
                    break
            if flag: #진실듣는사람이 있음
                how_many.extend(party)
                how_many = list(set(how_many)) #중복제거
    answer = 0
    for party in parties:
        flag = 0
        for member in party:
            if member in how_many:
                flag = 1
                break
        if flag == 0:
            answer += 1

    print(answer)

