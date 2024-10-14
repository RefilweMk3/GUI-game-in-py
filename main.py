import tkinter as tk
import random

def decide_winner(player_choice):
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    
    result = ""
    
    if player_choice == computer_choice:
        result = "Its a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        result = "You win!"
    else:
        result = "You lose!"
    
    result_label.config(text=f"Computer chose {computer_choice}. {result}")

def choose_rock():
    decide_winner("rock")

def choose_paper():
    decide_winner("paper")

def choose_scissors():
    decide_winner("scissors")

window = tk.Tk()
window.title("Rock Paper Scissors")

rock_button = tk.Button(window, text="Rock", width=15, command=choose_rock)
rock_button.pack(pady=10)

paper_button = tk.Button(window, text="Paper", width=15, command=choose_paper)
paper_button.pack(pady=10)

scissors_button = tk.Button(window, text="Scissors", width=15, command=choose_scissors)
scissors_button.pack(pady=10)

result_label = tk.Label(window, text="Make your choice!", font=("Arial", 14))
result_label.pack(pady=20)

window.mainloop()
