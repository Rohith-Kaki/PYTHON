def shark_horn(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end=" ")
        for j in range(i+1):
            print("*",end="")
        print()
n = int(input("Ener number of rows:"))
shark_horn(n)