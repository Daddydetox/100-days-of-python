import random

word_list = ["aardvark", "baboon", "camel"]
display = []
lives = 7

chosen_word = list(random.choice(word_list))

print(f"The chosen word is: {chosen_word}")

for letter in chosen_word:
    display += "_"

while display != chosen_word and lives > 0:
    print(display)
    print(f"Lives left: {lives}\n")

    guess = input("Guess a letter: ").lower()

    if guess in chosen_word:
        for i in range(len(chosen_word)):
            letter = chosen_word[i]
            if letter == guess:
                display[i] = guess
    else:
        lives -= 1
        print("\nIncorrect guess! You lost a life.")

if display == chosen_word:
    print(f"Congratulations! You guessed the word {''.join(chosen_word).upper()} correctly.")
else:
    print(f"Too bad! You lost. The right word was: {''.join(chosen_word).upper()}")