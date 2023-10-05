# Write a program to print the given pattern.
# A 
# B C 
# D E F 
# G H I J
# K L M N O


alphabet = 65
for i in range(0,5):
  for j in range(0,i+1):
   letter = chr(alphabet)
   print(letter,end=" ")
   alphabet += 1
  print()
    