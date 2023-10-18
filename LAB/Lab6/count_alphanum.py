# Write a program that accepts a sentence and calculate the number of letters and digits.
# 	Sample Input  hello world! 123
# 	Output  LETTERS - 10, DIGITS – 3, Punctuations – 1
def alphanum (sentence):
    alpha = 0
    num = 0
    special_char = 0
    for char in sentence:
        if char.isalpha():
            alpha += 1
        elif char.isdigit():
            num+=1
        else:
            if (char !=" "):  
                special_char+=1
    return f"Letters - {alpha}, numbers - {num}, special_character - {special_char}"
sentence = input("Enter a sentence with letter, numbers and special characters:")
print(alphanum(sentence))