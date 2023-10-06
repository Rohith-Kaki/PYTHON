# Write a program that accepts a sentence and calculate the number of letters and digits. You cannot use isumeric(), isalpha(), isdigit()
Sentence = input("Enter a sentence with letters and numbers:")
count_alp = 0
count_num = 0
for i in Sentence:
    if(ord(i)>=65 and ord(i)<=90):
        count_alp+=1
    elif(ord(i)>=97 and ord(i)<=122):
        count_alp+=1
    elif(ord(i)>=48 and ord(i)<=57):
        count_num+=1
  
print(f"Alphabets in sentence are {count_alp} ")
print(f"Numbers in sentence are {count_num}")