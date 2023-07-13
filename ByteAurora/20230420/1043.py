people_count, party_count = map(int, input().split(' '))

truth_knowers = set(input().split(' ')[1:])  # 진실을 아는 사람 목록
parties = []

for _ in range(0, party_count):
    parties.append(set(input().split(' ')[1:]))

filtered_parties = []  # 필터링된 파티

new_knower_found = True  # 진실을 아는 새로운 사람이 발견되었는지에 대한 여부

while new_knower_found:  # 진실을 아는 새로운 사람이 발견되지 않았을 때까지 반복
    new_knower_found = False

    filtered_parties = parties[:]
    for party in parties:  # 현재 남아있는 모든 파티를 조사
        if party.intersection(truth_knowers):  # 만약 파티 멤버 중 진실을 아는 사람이 있을 경우
            new_knower_found = True
            truth_knowers = truth_knowers.union(party)
            filtered_parties.remove(party)
    parties = filtered_parties[:]

print(len(parties))
