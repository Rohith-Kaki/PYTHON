# Write a program to display only those numbers from a list that satisfy the following conditions
# numbers = [12, 75, 150, 175, 0, 134, 50, 510, 100, 125]
# 	a.	The number must be divisible by five
# 	b.	If the number is greater than 150, then skip it and move to the next number
# 	c.	If the number is greater than 500, then stop the loop

numbers = [12, 75, 150, 175, 0, 134, 50, 510, 100, 125]
#Part a.
for i in range(0,len(numbers)):
  if(numbers[i]%5 == 0):
    print(numbers[i],"Number is divisible by 5\n")
  else:
    print(numbers[i],"Number is not divisible\n")
#Part b.
for i in range(0,len(numbers)):
  if(numbers[i]>150):
    continue
  else:
    print(numbers[i],"Number is less than 150\n")

#Part c.
for i in range(0,len(numbers)):
  if(numbers[i]>500):
    break
  else:
    print(numbers[i],"Number is less than 500\n")