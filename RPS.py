import random
print("----------Welcome to the Rock * Paper * Scissor Game!!--------------")
user_wins = 0
computer_wins = 0
options = ["Rock","Paper","Scissor"]

while True:
    print(" ")
    print("Type R for Rock , P for Paper , S for Scissor ")
    print(" ")
    user_input = input("Type R/P/S or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in ["r","p","s"]:
        print("Please Input a valid input")
        continue

    random_number = random.randint(0,2)
    # Rock: 0, Paper: 1, Scissor: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "r" and computer_pick == "Scissor":
        print("You WON!")
        user_wins +=1

    elif user_input == "p" and computer_pick == "Rock":
        print("You WON!")
        user_wins +=1

    elif user_input == "s" and computer_pick == "Paper":
        print("You WON!")
        user_wins +=1

    elif user_input == "s" and computer_pick == "Scissor":
        print("Draw!")

    elif user_input == "r" and computer_pick == "Rock":
        print("Draw!")

    elif user_input == "p" and computer_pick == "Paper":
        print("Draw!")

    else:
        print("You LOST!")
        computer_wins +=1

print(" ")
print("You won", user_wins , "Times.")
print("Computer won" , computer_wins , "Times.")
print("Thank You! Bye!")