import random

# ASCII art for the game logo
logo = """
.------.
|A_  _ |.
|( \/ ).-----.
| \  /|K /\  |
|  \/ | /  \ |
`-----| \  / |
      |  \/ K|
      `------'
"""


# Function to draw a card from the deck
def drawCard(hand):
    hand.append(random.choice(cards))


# Function to deal the starting hand for player and dealer
def dealStartingHand():
    for _ in range(2):
        drawCard(playerCards)
        drawCard(dealerCards)


# Function to calculate the score of a hand and handle changing 11 to 1
def calculateScore(hand):
    score = sum(hand)

    # Handle changing 11 to 1 if score is over 21
    if 11 in hand and score > 21:
        hand[hand.index(11)] = 1
        score = sum(hand)

    return score


# List of possible card values
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
playerCards = []
dealerCards = []

# Initial player cash
playerCash = 1000

# Main game loop
while playerCash > 0:
    print(logo)
    print(f"Your cash: {playerCash}$")
    bet = int(input("Place your bet (max 200): "))
    if bet > playerCash:
        print("You don't have enough cash for that bet.")
        continue
    elif bet > 200:
        print("Maximum bet is 200.")
        continue

    playerCash -= bet

    playerCards.clear()
    dealerCards.clear()

    dealStartingHand()
    playerScore = calculateScore(playerCards)
    dealerScore = calculateScore(dealerCards)

    print(f"\nDealer:\t[{dealerCards[0]}, X]")
    print(f"You:\t{playerCards} ({playerScore})")

    # Check for player's Blackjack or bust
    if playerScore == 21:
        print("Blackjack! You win.")
        playerCash += 2 * bet
        continue
    else:
        # Player draws cards
        while input(f"You have {playerScore}. Press [1] to draw more or anything else to stop: ") == "1":
            drawCard(playerCards)
            playerScore = calculateScore(playerCards)
            print(f"You:\t{playerCards} ({playerScore})")

            if playerScore > 21:
                print(f"{playerScore}, too bad. You lose.")
                break
            elif playerScore == 21:
                break

        if playerScore <= 21:
            # Dealer draws cards if needed
            while dealerScore < 17:
                drawCard(dealerCards)
                dealerScore = calculateScore(dealerCards)

            # Compare scores and determine the winner
            print(f"Dealer:\t{dealerCards} ({dealerScore})")
            if dealerScore > 21:
                print(f"Dealer has {dealerScore} and is bust. You win!")
                playerCash += 2 * bet
            elif playerScore == dealerScore:
                print(f"It's a tie!")
                playerCash += bet
            elif playerScore > dealerScore:
                print(f"You win!")
                playerCash += 2 * bet
            else:
                print(f"You lose.")

print("Game over. Thanks for playing!")
