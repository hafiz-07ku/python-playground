from art import blackJackLogoLogo
import random
import os
print(blackJackLogoLogo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

dealerCards = []
playerCards = []

def handTotal(hand):
    return sum(hand)

def dealCards(hand):
    chosenCard = random.choice(cards)
    if chosenCard == 11 and handTotal(hand) + chosenCard > 21:
        chosenCard = 1
    hand.append(chosenCard)

def winner():
    if handTotal(playerCards) > 21:
        print(f"Your final hand: {playerCards}, final score: {handTotal(playerCards)}")
        print(f"You are bust 😭. You have lost the game")
    elif handTotal(dealerCards) > 21:
        print(f"Your final hand: {playerCards}, final score: {handTotal(playerCards)}")
        print(f"Dealer is bust 😎. You have won the game")
    elif handTotal(playerCards) > handTotal(dealerCards):
        print(f"Your final hand: {playerCards}, final score: {handTotal(playerCards)}")
        print(f"Dealer's final hand: {dealerCards}, final score: {handTotal(dealerCards)}")
        print("You win 😎")
    elif handTotal(playerCards) < handTotal(dealerCards):
        print(f"Your final hand: {playerCards}, final score: {handTotal(playerCards)}")
        print(f"Dealer's final hand: {dealerCards}, final score: {handTotal(dealerCards)}")
        print("You lose 😭")
    else:
        print(f"Your final hand: {playerCards}, final score: {handTotal(playerCards)}")
        print(f"Dealer's final hand: {dealerCards}, final score: {handTotal(dealerCards)}")
        print("It's a tie")
def clear():
    os.system('clear')


def gameStart():
    playerCards.clear()
    dealerCards.clear()
    dealCards(playerCards)
    dealCards(dealerCards)
    dealCards(playerCards)
    dealCards(dealerCards)
    print(f"Dealer's first card: {dealerCards[0]}")
    print(f"Your cards: {playerCards}, current score: {handTotal(playerCards)}")

    if handTotal(dealerCards) == 21:
        print("Dealer has BlackJack. You lose 😭")
    elif handTotal(playerCards) == 21:
        print("You have BlackJack. You win 😍")
    else:
        while handTotal(playerCards) < 21:
            hitOrStand = input("Type 'y' to get another card(Hit), type 'n' to Stand: ")
            if hitOrStand.lower() == 'y':
                dealCards(playerCards)
            else:
                break
        if handTotal(playerCards) > 21:
            print("You are bust. You lose 😭")
        else:
            while handTotal(dealerCards) < 17:
                dealCards(dealerCards)
        winner()

gameStart()
while True:
    playAgain = input('Type "y" to play afresh and "n" to quit: ').lower()

    if playAgain == 'n':
        print("Thanks for playing!")
        break
    else:
        clear()
        gameStart()