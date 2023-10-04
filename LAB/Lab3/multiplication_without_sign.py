def mlutiply_by_two(number):      #defining function by user 
    shifted_number = number<<1    #Left_Shift by 1
    return shifted_number
number = int(input("Enter a number to be multiplied by 2:"))
result = mlutiply_by_two(number)
print(f"The product of 2 and {number} is {result}")   #f-Stings
