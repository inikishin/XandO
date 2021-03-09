# init vars
pole = [['-' for x in range(3)] for y in range(3)]
game_history = {}
player1 = {'label': '', 'value': 'x'}
player2 = {'label': '', 'value': 'o'}


def print_pole():
    print('Game pole:')
    print('\t   1 2 3')
    for i in range(3):
        print(f'\t{i + 1} ', pole[i][0], pole[i][1], pole[i][2])


def print_rules():
    print('Game rules:'
          '\n\t enter cell coordinate with space, for example "1 1"'
          '\n\t type "pole" to see pole'
          '\n\t type "hist" to see current game history'
          '\n\t type "stop" to terminate current game')


# print current game steps history
def print_hist():
    print('Current game history:')
    for k, i in game_history.items():
        print(f"\tStep {k + 1} - Player {i['player']} point '{i['value']}' at {i['coords'][0]}")


# Check win condition for current player
def check_win(player):
    for i in range(3):
        if all(pole[i][j] == player['value'] for j in range(3)):  # check horizontal row
            return True
        if all(pole[j][i] == player['value'] for j in range(3)):  # check vertical column
            return True

    if all(pole[i][i] == player['value'] for i in range(3)): # check main diagonal
        return True
    if all(pole[2-i][i] == player['value'] for i in range(3)): # check back diagonal
        return True
    return False



# Process input from player
def process_input(player):
    while True:
        step = input(f"{player['label']} ({player['value']}), your step now (or ask help '?'): ")
        if step == '?':
            print_rules()
        elif step == 'pole':
            print_pole()
        elif step == 'hist':
            print_hist()
        elif step == 'stop':
            return False
        elif len(step.split()) == 2:
            step_list = step.split()
            if step_list[0] in ['1', '2', '3'] and step_list[1] in ['1', '2', '3']:
                if pole[int(step_list[0]) - 1][int(step_list[1]) - 1] == '-':
                    make_step(step_list, player)
                    return True
                else:
                    print('This cell already filled')
            else:
                print('Coords values out of range!')
        else:
            print('Unknown command')


# make a step
def make_step(step, player):
    pole[int(step[0]) - 1][int(step[1]) - 1] = player['value']
    if len(game_history.keys()) == 0:
        game_history[0] = {'player': player['label'], 'value': player['value'], 'coords': [step]}
    else:
        game_history[list(game_history.keys())[-1] + 1] = {'player': player['label'], 'value': player['value'],
                                                           'coords': [step]}


if __name__ == '__main__':
    print('Welcome to the Game!')
    print_rules()
    player1['label'] = input('Player 1 pls enter your name: ')
    player2['label'] = input('Player 2 pls enter your name: ')
    print_pole()
    curr_player = player1
    while True:
        if not process_input(curr_player):
            print('Game stopped')
            break
        print_pole()
        if check_win(curr_player):
            print(f"Player {curr_player['label']} WINS!")
            break
        if '-' not in str(pole):
            print('Draw - Game over')
            break
        curr_player = player1 if curr_player == player2 else player2
    # TODO: добавить ai
