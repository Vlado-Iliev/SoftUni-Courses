cards = input().split(' ')
team_a = 11
team_b = 11
kicked_players = []
game_terminated = False

for card in cards:
    current = card.split('-')
    if current[0] == 'A':
        if current[1] not in kicked_players:
            kicked_players += current[1]
            team_a -= 1
    elif current[0] == 'B':
        if current[1] not in kicked_players:
            kicked_players += current[1]
            team_b -= 1
    if team_a < 7 or team_b < 7:
        game_terminated = True
        break

print(f'Team A - {team_a}; Team B - {team_b}')

if team_a < 7 or team_b < 7:
        print('Game was terminated')
