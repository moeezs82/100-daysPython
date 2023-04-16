import random
import sys

questions_list = ["Question 1", "Question 2",
                  "Question 3", "Question 4", "Question 5", "Question 6"]
correct_answer_list = ["Correct 1", "Correct 2",
                       "Correct 3", "Correct 4", "Correct 5", "Correct 6"]
price_amount = [100, 150, 200, 270, 400, 550]
win_amount = 0


def checkAnswer(given_answer, correct_answer, amount, question):
    '''takes user's answer, correct answer, previous question price(which is useable after 3 questions)
    and question index and return boolean accordingly, futhermore it also check condition for amount
    deduction and calculates the amount'''
    global win_amount
    print(given_answer, correct_answer)
    if given_answer != correct_answer:
        print("Oops! Answer is not correct")
        if question >= 3:
            print(f"\nAs per rule ${amount} will be deducted") # modified f string from next tut
            win_amount -= amount
        return False
    return True


print("*****Welcome to KBC!*****")
print("we will ask 6 question with their option a, b, c and d select from given options one option is correct rest are wrong...")

total_amount = 0
for i in range(len(price_amount)):
    total_amount += price_amount[i]
print("On Wrong Answer the program will exit and you take win amount or you can play it to the end to win $" + str(total_amount))
while True:
    play = input("Please enter c to countinue and e for exit: ")

    if (play == "c"):
        print("Here is your first question!")
        break
    elif (play == "e"):
        print("press f5 to start over")
        sys.exit()
    else:
        print("\n***Invalid input***\n")

# creating options for each question and shuffling it
options_dict = {}
for question in range(len(questions_list)):
    options_dict[question] = [
        'Correct '+(str(question+1)), 'Wrong Answer', 'Wrong Answer', 'Wrong Answer']
    random.shuffle(options_dict[question])

    while True:
        # priting question and option and asking for input
        print(questions_list[question])
        print(options_dict[question])
        answer = input('Enter a, b, c, or d: ')
        # if answer is from given input then breaking while loop otherwise infinite loop
        if (answer == 'a' or answer == 'b' or answer == 'c' or answer == 'd'):
            break
        else:
            print("\n***Invalid input***\n")
    # checking for correct answer
    if (answer == 'a'):
        print('Your Answer:', options_dict[question][0])
        # breaking for loop if answer is not correct
        check_answer = checkAnswer(options_dict[question][0], correct_answer_list[question], price_amount[question-1], question)
        if not check_answer:
            break
    elif (answer == 'b'):
        print('Your Answer:', options_dict[question][1])
        # breaking for loop if answer is not correct
        check_answer = checkAnswer(options_dict[question][1], correct_answer_list[question], price_amount[question-1], question)
        if not check_answer:
            break
    elif (answer == 'c'):
        print('Your Answer:', options_dict[question][2])
        # breaking for loop if answer is not correct
        check_answer = checkAnswer(options_dict[question][2], correct_answer_list[question], price_amount[question-1], question)
        if not check_answer:
            break
    elif (answer == 'd'):
        print('Your Answer:', options_dict[question][3])
        # breaking for loop if answer is not correct
        check_answer = checkAnswer(options_dict[question][3], correct_answer_list[question], price_amount[question-1], question)
        if not check_answer:
            break
    else:
        print("Something went wrong!")
        break

    # we are out side if conditions means answer is correct so adding question price in wi amount
    win_amount += price_amount[question]
    print("Correct Answer Congratulations...\n")

    # adding extra condition after 3 question to deduct amount
    if (question == 3):
        # using ANSI escape codes to make precaution red color background
        print(f"\033[41mPrecaution!!\033[0m Your have won ${win_amount} from now on if you answer wrong previous amount will deducted from win amount") # modified f string from nect tut
        input("Enter any key to continue: ")

    # asking for next question
    # making infinite loop to take valid input
    while True:
        play_next = input(f"You have won ${win_amount} c to continue e for exit: ")
        # exiting loop if get correct input
        if (play_next == 'c' or play_next == 'e'):
            break
        else:
            print("\n***Invalid input***\n")

    # break for loop if not next question
    if (play_next == 'e'):
        break

print(f"Congratulations you won ${win_amount}")
print("\nPress f5 to play again")
