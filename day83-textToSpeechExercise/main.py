import win32com.client as wincom

# you can insert gaps in the narration by adding sleep calls
import time

speak = wincom.Dispatch("SAPI.SpVoice")

text = "Welcome to text to speech program"

print("***Welcome to text to Speech***\n")
speak.Speak(text)

# 3 second sleep
while True:
    time.sleep(1) 
    speak.Speak("Enter 'Y' to use program 'E' to exit")
    choice = input("Enter y to use program e to exit: ").lower()
    if choice == "y":
        speak.Speak("Please Enter Your Text")
        text = input("Please Enter Your Text: ").lower()
        speak.Speak(text)
    elif choice == "e":
        break
    else:
        speak.Speak("Invalid choice")
        print("Invalid Input!\n")

 

speak.Speak("Thank you for using this program")
print("Thank you for using this program")