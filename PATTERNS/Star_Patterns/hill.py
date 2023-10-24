def hill(n):
    for i in range(n):
        for j in range(n-i-1): # i for rows j for coloums and spaces.
            print(" ",end=" ")
        for j in range(i+1):
            print("*",end=" ")
        for j in range(i):
            print("*",end=" ")
        print()
n = int(input("Entter number of rows:"))
hill(n)
