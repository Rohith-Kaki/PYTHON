def square(n):
    for i in range(n):  #i for rows and j for coloums.
        for j in range(n):
            print("*",end =" ")
        print()
n = int(input("Enter size of aquare: "))
square(n)
