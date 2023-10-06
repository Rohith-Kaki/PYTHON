#Write a Python program that takes a list of words (user input one by one) use space to stop and returns the length of the longest one (Hint: Use isspace() ).
print("Enter Name to START and Space to STOP:")
Name = " "
list = []
long_word = 0
count_index = -1                #As the list, printed in line 10 is from [stating:(end-1)].
while Name:
    Name = input("Enter a word:")
    list.append(Name)
print(list[:-1])
for name in list:                #Takes each item from the list.
    if(long_word<len(name)):
        long_word = len(name)
     
print(f"The length of longest word entered is {long_word}")
for name in list:                 #Prints the word with longest length.
    if(long_word != len(name)): 
        count_index += 1
        continue
    print(f"Tke longest word enterd is {list[count_index+1]}")
 




