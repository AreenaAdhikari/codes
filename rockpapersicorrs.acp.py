import tkinter as tk
import random 
root = tk.Tk()
root.title('Rock paper Scissors')
root.geometry("250x200")
choices = ["Rock","Paper","Scissors"]
result = tk.Label(root, text="", font=("Arial",12))
result.pack(pady=20)

def play(user_choice):
    computer = random.choice(choices)
    if user_choice == computer:
        outcome = "Draw"
    elif (user_choice == "Rock" and computer == "Scissors") or \
          (user_choice == "Paper" and computer == "Rock") or \
          (user_choice == "Scissors" and computer == "Paper"):
        outcome = "You Win!"
    else:
        outcome = "Computer Wins!"
    result.config(text=f"You: {user_choice}\nComputer: {computer}\n{outcome}")

tk.Button(root, text="Rock", width=10, command=lambda: play("Rock")).pack(pady=5)
tk.Button(root, text="Paper", width=10, command=lambda: play("Paper")).pack(pady=5)
tk.Button(root, text="Scissors", width=10, command=lambda: play("Scissors")).pack(pady=5)

root.mainloop()