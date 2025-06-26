import random

# stone : 1 , scissor: -1 , paper : 0
computer = random.choice([1, -1, 0])

you = int(input("Enter your turn (1 = Stone, -1 = Scissor, 0 = Paper): "))

if you not in [1, -1, 0]:
    print("Invalid input!")
else:
    print(f"Computer chose: {computer}")

    if you == computer:
        print("You both are tied")
    elif (computer == 1 and you == -1) or \
         (computer == -1 and you == 0) or \
         (computer == 0 and you == 1):
        print("You lose!")
    else:
        print("You win!")
    input("\nPress Enter to exit...")