def is_even(n):
    if(n==0):
        return "even"
    else:
        return is_odd(n-1)
def is_odd(n):
    if(n==0):
        return "odd"
    else:
        return is_even(n-1)
number = int(input("Enter a number:"))
print(is_even(number))