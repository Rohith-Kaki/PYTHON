#WAP to swap the numbers given by the user
a = int(input("Enter a number A:"))
b = int(input("Enter a number B:"))
a = a+b
b = a-b 
a = a-b
print("Number A:{0}\nNumber B:{1}".format(a,b))