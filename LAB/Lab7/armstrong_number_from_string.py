# 2.From Question 1. If it is a number, check whether the number is an Armstrong numbers or not and print the same.
def print_digits_armstrong(sentence):
    numbers = []
    for char in sentence:
        if 'a' <= char.lower() <= 'z':
            continue
        elif '0' <= char <= '9':
            print(char,end="")
            numbers.append(char)
    print()
    joined_numbers = int("".join(numbers))
    number_length = len(numbers)
    sum_of_cubes = 0
    for number in numbers:
        sum_of_cubes += int(number) ** number_length
    if(sum_of_cubes == joined_numbers):
        print("Armstrong number")
    else:
        print("Not an armstrong number")
sentence = input("Enter a sentence: ")
print_digits_armstrong(sentence)
