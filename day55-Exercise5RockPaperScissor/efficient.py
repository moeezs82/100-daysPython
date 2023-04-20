#                 R P S
# computer =      0 1 2
# player =  R  0  D L W
#           P  1  W D L
#           S  2  L W D

# using matrix
import random

results = ('Draw', 'Loose', 'Win'), ('Win', 'Draw',
                                     'Loose'), ('Loose', 'Win', 'Draw'), ('Win', 'Draw', 'loose')

user_win = 0
comp_win = 0


def getCheckWin(user: int, comp: int):
    # above matrix is set as user input is first then comp input
    global user_win
    global comp_win
    result = results[user][comp]
    if result.lower() == 'win':
        user_win += 1
        return 1
    if result.lower() == 'loose':
        comp_win += 1
        return -1

    return 0


while True:
    comp_choice = random.randint(0, 2)
    try:
        user_input = int(
            input("Enter 0 for ROCK, 1 for PAPER and 2 for SCISSOR: "))
        if user_input > 2 or user_input < 0:
            print('****Invalid Input****')
            continue
        print(
            f'\nyour input: {user_input} and computer choice: {comp_choice}\n')
        check_win = getCheckWin(user_input, comp_choice)
        if check_win == 0:
            print("Its a draw!")
        elif check_win == 1:
            print("Hurray! You win!")
        else:
            print("Computer wins")
        print(f"Your score: {user_win} and computer score: {comp_win}")
        play_again = input("To play again enter A: ").lower()
        if play_again == 'a':
            continue
        else:
            print(f"\nYour Final Score: {user_win-comp_win}")
            if user_win == comp_win:
                print("Game is draw")
            elif user_win > comp_win:
                print("Congratulations! You won!")
            else:
                print("Computer is over taking human race")
            break

    except ValueError:
        print("Error: Please enter only integer values.\n")
