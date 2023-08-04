import random

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

while True:
    user_choice = input('Type [0] for Rock, [1] for Paper, or [2] for Scissors (Q to quit): ').lower()

    if user_choice == 'q':
        break

    if user_choice not in {'0', '1', '2'}:
        print("Invalid choice. Please try again.")
        continue

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

    print(f"\nYou chose {choices[user_choice]['name']}")
    print(choices[user_choice]['art'])
    print(f"\nComputer chose {choices[computer_choice]['name']}")
    print(choices[computer_choice]['art'])
    print(f"{result} Score: {score}\n")

print("Thanks for playing!")
