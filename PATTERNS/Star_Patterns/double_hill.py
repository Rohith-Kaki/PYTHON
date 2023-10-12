def double_hill(n):
    for i in range(n-1):
        for j in range(n-i-1):
            print(" ",end="")
        for j in range(i+1):
            print("*",end=" ")
        for j in range(n-i-2):
            print(" ",end=" ") 
        for j in range(i+1):
            print("*",end=" ")
        print()
    for i in range(2*n-1):
        print("*",end=" ")

n = int(input("Enter number of rows:"))
double_hill(n)