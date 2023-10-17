# 3. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
# 	Sample Input: “hello world, This is python class”
# 	Output: hello world, T$is is pyt$on class
string = input("Enter a sentence:")
first_char = string[0]
print(string[0],end="")
for char in string[1:]:
    if (char == first_char):
        changed_char=char.replace(char,"$")
        print(changed_char,end="")
    else:
        print(char,end="")
                     