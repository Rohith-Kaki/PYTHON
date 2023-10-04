#WAP if a cashier has notes of denomination 10,50,100.If the amount to be withdrawn input through hunderds find the denomination of each note.
def calculate_notes(withdraw_amount):
    count_100 = 0
    count_50 = 0
    count_10 = 0
    change_amount = 0
    count_100 = withdraw_amount // 100
    remaining_amount = withdraw_amount % 100
    count_50 = remaining_amount // 50
    remaining_amount %= 50
    count_10 = remaining_amount // 10
    change_amount = remaining_amount % 10
    print("Number of Rs.100 notes:",count_100)
    print("Number of Rs.50 notes:",count_50)
    print("Number of Rs.10 notes:",count_10)
    print(f"Amount in coins {change_amount}")

withdraw_amount = int(input("Enter the amount to withdraw:"))
calculate_notes(withdraw_amount)
