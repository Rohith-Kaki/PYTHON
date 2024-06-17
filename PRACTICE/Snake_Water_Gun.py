# matrix =       S  W  G
#               -1  0   1
#         S -1   D  W   L
#         W 0    L   D  W
#         G 1    W   L  D
import random
result = [["Draw", "Win", "Loose"],
          ["Loose", "Draw", "Win"],
          ["Win", "Loose", "Draw"]]
while(True):
    print("Enter your choice to Start, to quit press 3:")
    user_choice= int(input(" 0.Snake\n 1.Water\n 2.Water\n 3.Quit\n"))
    if(user_choice == 3):
        print("Thank you for playing, Come back Soon")
        break
    while user_choice not in range(0,3):
        print("Enter a Valid choice")
        user_choice= int(input(" 0.Snake\n 1.Water\n 2.Water\n 3.Quit\n"))
        if(user_choice == 3):
            print("Thank you for playing, Come back Soon")
            break
    computer = [0,1,2]
    computer_choice = random.choice(computer)
    # if(computer_choice == 0):
    #     print("Computer choosed Snake")
    # elif(computer_choice == 1):
    #     print("Computer choosed Water")
    # else:
    #     print("Computer choosed Gun")
    # print(computer_choice)
    # print(user_choice)
    if(user_choice == computer_choice):
        print(result[user_choice][computer_choice])
    elif(user_choice > computer_choice):
        print(result[user_choice][computer_choice])
    else:
        print(result[user_choice][computer_choice])