import random
import tkinter as tk
from tkinter import messagebox

choices = {
    0: {"name": "Rock", "art": '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''},
    1: {"name": "Paper", "art": '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''},
    2: {"name": "Scissors", "art": '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''}
}

score = 0

def play_game():
    global score
    user_choice = user_var.get()
    user_choice = int(user_choice)

    computer_choice = random.randint(0, 2)

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice - computer_choice) % 3 == 1:
        result = "You win!"
        score += 1
    else:
        result = "You lost!"
        score -= 1

    result_label.config(text=result)
    score_label.config(text=f"Score: {score}")

    user_art_label.config(text=choices[user_choice]['art'])
    computer_art_label.config(text=choices[computer_choice]['art'])

def quit_game():
    if messagebox.askokcancel("Quit", "Do you want to quit the game?"):
        root.destroy()

# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")
root.geometry("400x600")  # Set a fixed window size
root.minsize(400, 600)    # Set the minimum size for the window

# Disable resizing of the window
root.resizable(False, False)

# User choice label and variable
user_label = tk.Label(root, text="Select your choice:")
user_label.pack()

user_var = tk.StringVar()
user_var.set("0")  # Default choice: Rock

# User choice buttons
for i in range(3):
    tk.Radiobutton(root, text=choices[i]['name'], variable=user_var, value=str(i)).pack()

# Play button
play_button = tk.Button(root, text="Play", command=play_game)
play_button.pack()

# Result label
result_label = tk.Label(root, text="", font=("Helvetica", 16, "bold"))
result_label.pack()

# User and computer choices artwork labels
user_art_label = tk.Label(root, text="", font=("Courier New", 12), anchor=tk.CENTER)
user_art_label.pack()

computer_art_label = tk.Label(root, text="", font=("Courier New", 12), anchor=tk.CENTER)
computer_art_label.pack()

# Score label
score_label = tk.Label(root, text="Score: 0", font=("Helvetica", 14))
score_label.pack()

# Quit button
quit_button = tk.Button(root, text="Quit", command=quit_game)
quit_button.pack()

root.protocol("WM_DELETE_WINDOW", quit_game)  # Handle window close button

root.mainloop()