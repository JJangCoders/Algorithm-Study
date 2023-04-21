from sys import stdin

#Thanks to YoungJin, I now use dictionary to solve problems

# 6 5
# 1 6
# 2 4 5
# 2 1 2
# 2 2 3
# 2 3 4
# 2 5 6

N, M = map(int, stdin.readline().split())   #first line input

people_who_know_the_truth_list = list(map(int, stdin.readline().split()))   #second line input

people_to_avoid_lying = {}  #dictionary to store people to avoid lying to
party_people_2nd_array_list = []
number_of_party_with_lie = 0
party_truth_flag = False    #flag to indicate weather Jimin can lie or not

if len(people_who_know_the_truth_list) == 1:    #no one knows the truth
    number_of_party_with_lie = M
    for i in range(M):
        party_people_2nd_array_list.append(list(map(int, stdin.readline().split())))
else:
    people_who_know_the_truth_list = people_who_know_the_truth_list[1:] #slicing the number of people

    for person in people_who_know_the_truth_list:
        people_to_avoid_lying[person] = True

    for i in range(M):  #loop to register people in the dictionary
        party_people = list(map(int, stdin.readline().split()))
        party_people_2nd_array_list.append(party_people[1:])

    for i in range(M):
        for j in range(M):
            party_truth_flag = False    #flag to indicate whether Jimin can lie or not
            for person in party_people_2nd_array_list[j]:
                if people_to_avoid_lying.get(person):
                    party_truth_flag = True
                    break
            if party_truth_flag:
                for person in party_people_2nd_array_list[j]:
                    if people_to_avoid_lying.get(person) is None:
                        people_to_avoid_lying[person] = True
    

    for i in range(M):
        party_truth_flag = False
        for person in party_people_2nd_array_list[i]:
            if people_to_avoid_lying.get(person):
                party_truth_flag = True
                break
        if party_truth_flag == False:
            number_of_party_with_lie += 1

print(number_of_party_with_lie)