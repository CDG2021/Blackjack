from psutil import users
from sqlalchemy import false, true
from art import logo
from gameEngine import BlackJack
import os

clear = lambda: os.system('cls')
gameFunctions = BlackJack()

def gameRunning():
    print(logo)

    userCards = []
    computerCards = []
    gameOver = False

    for _ in range(2):
        userCards.append(gameFunctions.dealCards())
        computerCards.append(gameFunctions.dealCards())

    while not gameOver:
        userScore = gameFunctions.calculateScore(userCards)
        computerScore = gameFunctions.calculateScore(computerCards)
        print(f"   Your cards: {userCards}, current score: {userScore}")
        print(f"   Computer's first card: {computerCards[0]}")

        if userScore == 0 or computerScore == 0 or userScore > 21:
            gameOver = True
        else:
            userDeal = input("Type 'y' to get another card, type 'n' to pass: ")
            if userDeal == "y":
                userCards.append(gameFunctions.dealCards())
            else:
                gameOver = True
    
    while computerScore != 0 and computerScore < 17:
        computerCards.append(gameFunctions.dealCards())
        computerScore = gameFunctions.calculateScore(computerCards)

    print(f"   Your final hand: {userCards}, final score: {userScore}")
    print(f"   Computer's final hand: {computerCards}, final score: {computerScore}")
    print(gameFunctions.compare(userScore, computerScore))

while input("Do you want to play a game of Blackjack? type 'y' or 'no': ") == "y":
    clear()
    gameRunning()