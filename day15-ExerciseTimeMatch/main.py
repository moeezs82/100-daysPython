import re
import datetime

while True:
    time_zone = input(
        "To go with current time input y, and n to input custom time: ")

    if (time_zone == 'y'):
        now = datetime.datetime.now().time()
        print("Current Time: ", now)
        if now.hour < 12:
            print("Good morning!")
        elif now.hour < 18:
            print("Good afternoon!")
        else:
            print("Good night!")
        break
    elif (time_zone == 'n'):
        while True:
            user_time = input("Enter time in format 'HH:MM AM or PM': ")
            pattern = r'^\d{1,2}:\d{2} (AM|PM)$'
            if re.match(pattern, user_time):
                given_time = datetime.datetime.strptime(user_time, '%I:%M %p').time()
                if given_time.hour < 12:
                    print("Good morning!")
                elif given_time.hour < 18:
                    print("Good afternoon!")
                else:
                    print("Good night!")
                break
            else:
                print("Invalid time format. Please enter the time in the format 'HH:MM AM or PM'.")
        break
    else:
        print("Invalid input")
