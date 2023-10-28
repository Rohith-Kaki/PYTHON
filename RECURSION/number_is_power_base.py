def number_is_power(number, base):
    if number == 1:     #if number is equal to 1 then it is base**0
        return True
    if number < base:   #when number is less than base and not equal to 1, it's not a power of the base
        return False
    if number % base == 0:
        return number_is_power(number // base, base)
    else:
        return False

number = int(input("Enter a number:"))
base = int(input("Enter a base:"))
print(number_is_power(number, base))