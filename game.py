from random import randint

game_running = True
game_results = []


def calc_monster_attack(attack_min, attack_max):
    return randint(attack_min, attack_max)


def game_ends(winner_name, loser_name):
    print(f'{winner_name} defeated {loser_name}!')


while game_running == True:
    counter = 0
    new_round = True

    player = {'name': 'Jordyn',
              'attack': 13, 'heal': 16, 'health': 100}
    monster = {'name': 'Max',
               'attack_min': 10, 'attack_max': 20, 'health': 100}

    print('---' * 7)
    print('Enter Player Name')
    player['name'] = input()

    print('---' * 7)
    print(player['name'] + ' has ' + str(player['health']) + ' health points')
    print(monster['name'] + ' the monster has ' +
          str(monster['health']) + ' health points')

    while new_round == True:
        counter = counter + 1
        player_won = False
        monster_won = False

        print('---' * 7)
        print('Make your move!')
        print('1) Attack')
        print('2) Heal')
        print('3) Exit Game')
        print('4) View High Scores')

        action_choice = input()

        if action_choice == '1':
            print('---' * 7)
            print('HIII-YAH!')
            print('*SLAM*')
            print('OUCH.')
            monster['health'] = monster['health'] - player['attack']

            if monster['health'] <= 0:
                player_won = True
            else:
                player['health'] = player['health'] - \
                    calc_monster_attack(
                        monster['attack_min'], monster['attack_max'])
                if player['health'] <= 0:
                    monster_won = True

        elif action_choice == '2':
            print('Healing in progress...')
            player['health'] = player['health'] + player['heal']
            print(player['name'] + ' now has ' +
                  str(player['health']) + ' health points left!')

            print('---' * 7)
            print('AHHH! Now ' + monster['name'] + 'is attacking!')
            player['health'] = player['health'] - \
                calc_monster_attack(
                    monster['attack_min'], monster['attack_max'])

            if player['health'] <= 0:
                monster_won = True

        elif action_choice == '3':
            new_round = False
            game_running = False

        elif action_choice == '4':
            for result in game_results:
                print(result)

        else:
            print('Invalid action.')

        if player_won == False and monster_won == False:
            print(monster['name'] + ' has ' +
                  str(monster['health']) + ' health points left...')
            print(player['name'] + ' has ' +
                  str(player['health']) + ' health points left...')

        elif player_won:
            game_ends(player['name'], monster['name'])
            round_result = {
                'name': player['name'], 'health': player['health'], 'moves': counter}
            game_results.append(round_result)

            new_round = False
            # makes us go back to the first while loop

        elif monster_won:
            game_ends(monster['name'], player['name'])
            round_result = {
                'name': player['name'], 'health': player['health'], 'moves': counter}
            game_results.append(round_result)

            new_round = False
            # makes us go back to the first while loop
