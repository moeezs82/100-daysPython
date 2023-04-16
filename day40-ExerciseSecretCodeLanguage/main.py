# problem statement
# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode


# my statement
# i made it little bit differently as the statement code will not decode the code that we encoded through it so i madeup some changes in decoding section

import random
import string

def encode_string(plain_text):
    array_to_encode = plain_text.split()
    encoded_array = []
    for string_to_encode in array_to_encode:
        if len(string_to_encode) <= 3:
            # adding three random characters at starting and at ending and changing the position of first latter to the end
            first_three_chars = ''.join(random.choice(
                string.ascii_lowercase) for _ in range(3))
            encoded_string = "{}{}{}{}".format(
                first_three_chars, string_to_encode[1:], string_to_encode[0], first_three_chars)
            encoded_array.append(encoded_string)
        else:
            # reversing the string
            encoded_array.append(string_to_encode[::-1])
    return " ".join(encoded_array)

def decode_string(encoded_string):
    array_to_decode = encoded_string.split()
    decoded_array = []
    for string_to_decode in array_to_decode:
        if len(string_to_decode) >= 7 and len(string_to_decode) <= 9:
            # this possibly 1 to 3 len characters that we encoded so checking if their first 3 and last 3 are equavalent
            first_three_chars = string_to_decode[:3]
            last_three_chars = string_to_decode[-3:]
            if first_three_chars == last_three_chars:
                middle_chars = string_to_decode[3:-3]
                # rephrasing as we change the position of first to last
                rephrase = "{}{}".format(middle_chars[-1], middle_chars[:-1])
                decoded_array.append(rephrase)
            else: # if not match means it is not encoded by our side so need to reverse
                decoded_array.append(string_to_decode[::-1])
        else:
            decoded_array.append(string_to_decode[::-1])
        
    return " ".join(decoded_array)



while True:
    task = input(
        "Enter E to encode text and D to decode text and T to terminate the program: ")
    if task.lower() == 't':
        break
    elif task.lower() == 'e':
        print("\nEnter the text you want to encode: ")
        text_to_encode = input()
        
        print("\nYour Encoded text is given below:\n")
        print(encode_string(text_to_encode))
        print()
    elif task.lower() == 'd':
        print("\nEnter the text you want to decode: ")
        text_to_decode = input()
        print("\nYour Decoded text is given below:\n")
        print(decode_string(text_to_decode))
        print()
    else:
        print("Invalid input. Please enter E, D or T.")
