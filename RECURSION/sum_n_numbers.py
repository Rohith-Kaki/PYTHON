def sum_numbers(n):
    if n <= 0:
        return n
    return n + sum_numbers(n-1)
n = int(input("Enter a number:"))
print(sum_numbers(n))