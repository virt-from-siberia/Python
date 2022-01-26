number_of_sticks = 10
player_turn = 1

while number_of_sticks > 0:
    print(f"how many sticks you take? Remaining : {number_of_sticks}")
    taken = int(input())
    if taken < 1 or taken > 3:
        print(f"You tried to take {taken}, but allowed are 1,2,3 sticks")
        continue

    number_of_sticks -= taken
    print(f"sticks taken: {taken} \n")

    if number_of_sticks <= 0:
        print(f"not more sticks in the game. \n player {player_turn} has lost")

    player_turn = 1 if player_turn == 2 else 2
