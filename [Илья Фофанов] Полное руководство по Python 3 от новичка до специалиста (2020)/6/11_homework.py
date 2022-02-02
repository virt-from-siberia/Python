board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ]


def print_state(state):
    for i, c in enumerate(state):
        if (i + 1) % 3 == 0:
            print(f"{c}")
        else:
            print(f"{c}|", end='')


print_state(board)

winning_combinations = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
]


def get_winner(state, combinations):
    for (x, y, z) in combinations:
        if state[x] == state[y] and state[y] == state[z] and (state[x] == 'X' or state[x] == 'O'):
            return state[x]

        return ''


def play_game(board):
    current_sign = 'X'

    while get_winner(board, winning_combinations) == '':
        index = int(input(f'Where do you want to draw {current_sign} ?'))
        board[index] = current_sign

        print_state(board)

        winner_sign = get_winner(board, winning_combinations)
        if winner_sign != '':
            print(f"We have a winner {winner_sign}")

        current_sign = 'X' if current_sign == 'O' else 'O'


play_game(board)
