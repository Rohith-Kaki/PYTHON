#WAP to accept a number and calculate the value of n+nn+nnn

n = int(input("Enter a number:"))
nn = int(str(n)+str(n))
nnn = int(str(n)+str(n)+str(n))
result = n+nn+nnn
print("The result if n+nn+nnn is:",result)