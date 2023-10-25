#Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
Word = input("Enter a Word:")
Word_len = len(Word)
if(Word_len >=3):
    if(Word[-3:] == "ing"):
        New_word = Word[:] +"ly"
        print(New_word)
    elif(Word[-3:] != "ing"):
         New_word = Word[:] + "ing"
         
         print(New_word)
elif(Word_len<3):
    print(Word) 
else:
    print("Invalid Input")