game_over = False
name = input("Greetings traveller! What is your name? ")
print(f"Welcome to Treasure Island {name}! Your goal is to find the treasure. Good luck!\n")

print("You come across two houses. One has many men inside it with rock solid abs, the other is filled with "
      "women, which do you enter?")

choice = input("[1] Enter the house with the men\n[2] Enter the house filled with women\n")

if choice == "1":
    print(
        "Walking into the gym. You do some bench presses and gain an incredible pump. Everyone applauds.")
    print("Someone approaches you.")
    print("Hello sugar! Would you like some performance enhancing drugs and a fun time?\n")
    choice = input("[1] Take the drugs\n[2] No drugs for me, I am natural!\n")
    if choice == "1":
        print("You overdose on pre-workout and die on the spot in heart failure.")
        print("The old man with a wig that gave you the drugs steals your wallet and buys soy for all your money.")
    elif choice == "2":
        print("Seeing that the girl is actually an old man with a wig, you suspect the worst and turn down the drugs.")
        print("Heading out from the gym you see a florist watering her flowers. A sudden urge to trample all her hard "
              "work kicks in.\n")
        choice = input("[1] Stomp on the flowers\n[2] Buy a flower and give it to her\n")
        if choice == "1":
            print("You jump up on the table and kicking and trampling her flowers like a donkey.")
            print("While kicking, you can see something in one of the pots.")
            print("It's dirt! Wow!")
            print(f"You win {name}! Enjoy your dirt.")
        elif choice == "2":
            print("She laughs you straight in the face and drag down your pants! What a loser!")
            print("Everybody on the street points at you and laughs.")
            print("You decide to end it later that evening by overdosing on lard.")
        else:
            print("Invalid input. Try again.")
    else:
        print("Invalid input. Try again.")

elif choice == "2":
    print(
        "You walk in to a party. You drink a beer and spend your last seconds in life regretting forgetting that "
        "you're allergic to social activities.")
else:
    print("Invalid input. Try again.")



