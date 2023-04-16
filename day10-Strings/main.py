string1 = '''this is 
muti"s line's
string'''

print(string1)

# string is like an array of characters
name="moeez"
print(name[1], '\n\n')

# iterate over each character in the string
for character in string1:
    # check if the character is a newline or a space
    if character != '\n' and character != ' ':
        print(character)
