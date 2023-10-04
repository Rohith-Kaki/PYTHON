#WAP which itrates from 1 to 50 and for multiples of 3 print"FIZZ" and for multiples of 5 print "BUZZ" and multiples of both print "FIZZBUZZ"

for p in range(1,51):
    if(p % 5 == 0 and p % 3 == 0):
        print("FIZZBUZZ")
    elif(p % 5 == 0):
        print("BUZZ")
    elif(p % 3 == 0):
        print("FIZZ")
    else:
        print(p)