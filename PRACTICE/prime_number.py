def prime_numbers(number):
    for number in range(2,number+1):
        if(number>1):
            is_prime=True
            for num in range(2,number):
                if (number%num == 0):
                     is_prime=False
                     break
        if(is_prime):
            print(number)
number = int(input("Enter a number:"))
(prime_numbers(number))