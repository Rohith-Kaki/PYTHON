# 1.Write a python program to read data from a string and check if data is string or numbers, print only numbers from the string.
def print_digits(sentence):
    for char in sentence:
        if 'a' <= char.lower() <= 'z':
            continue
        elif '0' <= char <= '9':
            print(char,end=" ")
sentence = input("Enter a sentence: ")
print_digits(sentence)


