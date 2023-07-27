import tkinter as tk
from tkinter import messagebox
import random

word_list = ["aardvark", "baboon", "camel"]
lives = 7

def choose_word():
    return random.choice(word_list)

def initialize_display(word):
    return ["_" for _ in word]

def check_guess(event=None):  # Pass the event parameter for binding
    global lives
    guess = guess_entry.get().lower()
    guess_entry.delete(0, tk.END)  # Clear the input field after each guess
    if len(guess) != 1 or not guess.isalpha():
        return
    if guess in chosen_word:
        for i in range(len(chosen_word)):
            letter = chosen_word[i]
            if letter == guess:
                display[i] = guess
    else:
        lives -= 1
        if lives == 0:
            game_over(False)
            return
    update_display()

    if "_" not in display:
        game_over(True)

def game_over(win):
    if win:
        messagebox.showinfo("Congratulations!", f"You guessed the word {''.join(chosen_word).upper()} correctly.")
    else:
        messagebox.showinfo("Too Bad!", f"You lost. The right word was: {''.join(chosen_word).upper()}.")
    window.destroy()

def update_display():
    display_label.config(text=" ".join(display))
    lives_label.config(text=f"Lives left: {lives}")

# Initialize the game
chosen_word = choose_word()
display = initialize_display(chosen_word)

window = tk.Tk()
window.title("Word Guessing Game")
window.geometry("400x200")  # Set the window size

# GUI Elements
display_label = tk.Label(window, text=" ".join(display), font=("Arial", 24))
display_label.pack(pady=10)

lives_label = tk.Label(window, text=f"Lives left: {lives}", font=("Arial", 14))
lives_label.pack(pady=5)

guess_entry = tk.Entry(window, font=("Arial", 16), width=1)  # Limit the width to 3 characters
guess_entry.pack(pady=10)
guess_entry.bind("<Return>", check_guess)  # Bind the Enter key to the check_guess function

guess_button = tk.Button(window, text="Guess", command=check_guess, font=("Arial", 14))
guess_button.pack(pady=5)

# Start the GUI
window.mainloop()
