"""Write a program to print multiplication table of a given number."""


a = int(input("Enter a number:"))
for i in range(1,11):
    print(str(a)+ "*" +str(i) + "=" +str(a*i))
