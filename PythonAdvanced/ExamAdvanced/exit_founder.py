current_player,next_player = input().split(', ')
size = 6

maze = [[col for col in input().split(' ')]for row in range(size)]
condition = {current_player: False, next_player: False}
while True:
    if condition[current_player]:
        condition[current_player] = False
        current_player, next_player = next_player, current_player
        move = [int(x) for x in input().strip('()').split(', ')]
        continue

    move = [int(x) for x in input().strip('()').split(', ')]
    place = maze[move[0]][move[1]]
    if place == 'W':
        print(f"{current_player} hits a wall and needs to rest.")
        condition[current_player] = True

    elif place == 'T':
        print(f'{current_player} is out of the game! The winner is {next_player}.')
        break
    elif place == 'E':
        print(f'{current_player} found the Exit and wins the game!')
        break


    current_player,next_player = next_player,current_player
