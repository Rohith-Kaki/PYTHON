#5. Write a python program to count repeated characters in a string and print count of each repeated character.

Sentence = input("Enter a sentence:")
count_char = {}
for char in Sentence:
    if char.isalpha():
        if char in count_char:
            count_char[char]+=1
        else:
            count_char[char]=1
for char,count in count_char.items():
    if count_char[char]>1:
        print(f"letter {char} is repeated {count} times")