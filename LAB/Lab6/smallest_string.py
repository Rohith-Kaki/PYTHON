#1.	Write a Python program that takes a list of words (user input one by one) use space to stop and returns the length of the smallest one (Hint: Use isspace() ).
word = input("Enter NAME to start and SPACE to stop:")
list_names = []
small = float("inf")
count = None
list_names.append(word)
while True:
    words = input("Enter a name:")
    if (words.isspace()):
        break
    list_names.append(words)
print(list_names)
for name in list_names:
    if(small>len(name)):
        small = len(name)
        count = list_names.index(name)


print(f"Smallest word is of length {small} and the word is {list_names[count]}")

