#WAP a program to subtract two numbers without using(-) sign.

a = int(input("Enter a number A:"))
b = int(input("Enter a number B:"))
diff = a+(~b+1)
print("The difference of {0} and {1} is {2}".format(a,b,diff))