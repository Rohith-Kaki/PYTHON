#Write a Python program to check if a string contains all letters of the alphabet (uppercase and lowercase both). Note: Can’t use isupper or islower functions.
def all_alphabet(input_string):
    all_case = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
    
    for char in all_case:
        if char not in input_string:
            return False
    return True

input_string = input("Enter a string :")

if (all_alphabet(input_string)):
    print("The sentece contains all alphabets upper and lower case.")
else:
    print("The sentence doesn't contain all upper case and lower case alphabets.")
    

