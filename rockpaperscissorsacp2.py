import random

choice1 = ["rock", "paper", "scissors"]

while True:
    users_choice = input("Pls can you choose rock, paper, or scissors (or 'quit' to exit): ").lower()
    
    if users_choice == "quit":
        print("Thank you for playing!")
        break
    
    if users_choice not in choice1:
        print("Invalid choice. Pleaseee try again.")
        continue
    
    computer_choice = random.choice(choice1)
    print(f"Computer chose: {computer_choice}")
    
    if users_choice == computer_choice:
        print("It's a tie!")
    elif (users_choice == "rock" and computer_choice == "scissors") or \
         (users_choice == "paper" and computer_choice == "rock") or \
         (users_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("Computer wins!")
    
    print()