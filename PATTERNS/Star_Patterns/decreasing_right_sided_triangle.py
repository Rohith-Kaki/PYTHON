def decreasing_right_sided_triangle(n):
    for i in range(n):  #i for rows and j for coloums.
        for j in range(i):
            print(" ",end=" ")
        for j in range(n-i):
            print("*",end=" ")
        print()
n = int(input("Ener number of rows:"))
decreasing_right_sided_triangle(n)
