import random
while True:
  user_actions = input("Enter your choice(rock,paper,scissors) : ")
  possible_actions = ["rock","paper","scissors"]
  computers_action = random.choice(possible_actions)
  print(f"'\nyour choice {user_actions}, computers choice {computers_action}\n")
  if user_actions == computers_action :
      print(f"Both chose {user_actions}. Its a tie c: yaya !!")
  elif user_actions == "rock":
     if computers_action == "scissors":
        print("Rock smahses scissor user wins.")
     else:
        print("Paper covers rock , You lose.")
  elif user_actions == "paper":
     if computers_action == "rock":
        print("Paper covers rock . You win")
     else:
        print("Scissors cuts paper . You lose.")
  elif user_actions == "scissors":
      if computers_action == "paper":
         print("Scissors cuts papper .,You win :)")
      else:
         print("Rock smashes paper,. yoU LOSE")
  play_again = input("PLAY again (y/n) : ")
  if play_again != "y": 
      break


