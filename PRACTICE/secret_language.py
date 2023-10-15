code_decode = input("Emter code or decode:")
if(code_decode == "code"):
    code_input = input("Enter the message to code:")
    splited_message = code_input.split(" ")
    list = []
    for word in splited_message:
        if (len(word)>=3):
            new_message = "rlp"+ word[1:]+word[0]+"sbp"
            list.append(new_message)
        else:
            new_message = word[::-1]
            list.append(new_message)
    print(" ".join(list))
elif(code_decode == "decode"):
    decode_input = input("Enter a message to decode:")
    splited_message = decode_input.split(" ")
    list = []
    for word in splited_message:
        if(len(word)>=3):
            new_word = word[3:-3]
            new_word = new_word[-1]+new_word[:-1]
            list.append(new_word)
        else:
            new_word = word[::-1]
            list.append(new_word)
    print(" ".join(list))