#Write a program which keeps accepting input from user until user enters zero (0). Print the sum and average of all the numbers.

a = int(input("Enter 1 to start\n0 to stop"))
sum = 0
list_number = []
while a != 0:
  a = int(input("Enter a number"))
  list_number.append(a)
  sum = sum+a
avg = sum/(len(list_number)-1)
print(sum)
print(avg)
#print(list_number)