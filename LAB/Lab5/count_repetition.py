#Write a Python program to count the number of characters (character frequency) in a string.
def character_frequency(input_string):
    character = {}
    for char in input_string:
        if char in character:
         character[char] += 1
        else:
           character[char] = 1
    for char, count in character.items():
        print(f"{char} is repeated {count} times.")

input_string = input("Enter letters to calculate repetition: ")
character_frequency(input_string)
