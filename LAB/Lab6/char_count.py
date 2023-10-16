#Given a string containing both upper and lower case letters. Write a Python program to count the number of repeated characters and display the maximum count of a character along with the character.
# Sample Input: ABaBCbGc
# 	Output:
# 	2A
# 	3B (three times B is repeated)
# 	2C
# 	1G
input_string = input("Enter the  string with both upper and lower case letters:")
input_string = input_string.upper()
count ={}
for char in input_string:
    if char.isalpha():
        if char in count:
            count[char]+=1
        else:
            count[char]=1
for count,char in count.items():
    print(f"{char} {count}")
