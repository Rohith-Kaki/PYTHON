def rectangle(n,m):
    for i in range(n):
        for j in range(m):
            print("*",end=" ")
        print()
length= int(input("Enter length of rectangle:"))
breadth = int(input("Enter breadth of ractangle:"))
rectangle(length,breadth)