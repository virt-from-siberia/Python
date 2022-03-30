from game_result import GameResult


def end_of_game_handler(result: GameResult):
    print(f'Questions asked:{result.questions_passed} . Mistakes made:{result.mistakes_made}')
    print(f"You won!" if result.won else 'You lost')
