import random

print('****ROCK PAPER SCISSOR****')
valid_inputs = {'r', 'p', 's'}

user_win = 0
comp_win = 0

def getCheckWin(comp: str, user: str):
    global user_win
    global comp_win
    # this is the draw case
    if comp == user:
        return 0
    # checking for user loseing case
    if comp == 'r' and user == 'p':
        comp_win+=1
        return -1
    if comp == 'p' and user == 's':
        comp_win+=1
        return -1
    if comp == 's' and user == 'r':
        comp_win+=1
        return -1
    # if none of above condition matches then user win
    user_win+=1
    return 1
    

while True:
    comp_choice = random.choice(list(valid_inputs))
    user_input = input("Enter R for ROCK, P for PAPER and S for SCISSOR: ").lower()
    if user_input not in valid_inputs:
        print('****Invalid Input****')
        continue
    print(f'\nyour input: {user_input} and computer choice: {comp_choice}\n')
    check_win = getCheckWin(comp_choice, user_input)
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
