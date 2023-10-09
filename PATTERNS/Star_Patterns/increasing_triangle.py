def increasing_triangle(n):
    for i in range(n):
        for j in range(i+1):  #or we can use range(i, n) starts at "i" and ends at "n-1"
            print("*",end=" ")
        print()
n = int(input("Ener number of rows:"))
increasing_triangle(n)