def NumberTrinagle(n):
    count = 100
    for i in range(n):
        for j in range(n-i):
            print(count, end= " ")
            count = count -1
        print()
NumberTrinagle(6)
