#WAP to print ARMSTRONG number
def is_armstrong_number(Number):
    num_str = str(Number)
    num_len = len(num_str)
    sum_of_cubes = 0
    for digit in num_str:
        sum_of_cubes += int(digit) ** num_len
    if(sum_of_cubes == Number):
        return True
    else:
        return False
    
Number = int(input("Enter a number:"))
if is_armstrong_number(Number):
    print(f"The number {Number} is armstrong")
else:
    print(f"The number {Number} is not Armsstrong")