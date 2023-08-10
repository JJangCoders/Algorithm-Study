from itertools import combinations
import sys


def get_ability_difference(synergy_map, team1, team2):
    def calculate_ability(team):
        return sum(synergy_map[i - 1][j - 1] + synergy_map[j - 1][i - 1] for i, j in combinations(team, 2))

    return abs(calculate_ability(team1) - calculate_ability(team2))


def get_min_ability_difference(player_count, synergy_map):
    min_ability_difference = float('inf')

    players = range(1, player_count + 1)
    team1_list = list(combinations(range(1, player_count + 1), player_count // 2))
    team1_list = team1_list[:len(team1_list) // 2]

    for team1 in team1_list:
        team2 = [player for player in players if player not in team1]

        ability_difference = get_ability_difference(synergy_map, team1, team2)

        if ability_difference < min_ability_difference:
            min_ability_difference = ability_difference

    return min_ability_difference


player_count = int(sys.stdin.readline())
synergy_map = [list(map(int, sys.stdin.readline().split())) for _ in range(player_count)]

print(get_min_ability_difference(player_count, synergy_map))
