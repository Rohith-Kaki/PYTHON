def reverse_hill(n):
    for i in range(n):
        for j in range(i):
            print(" ",end=" ")
        for j in range(n-i):
            print("*",end=" ")
        for j in range(n-i-1):
            print("*",end=" ")
        print()
n = int(input("Enter number of rows:"))
reverse_hill(n)