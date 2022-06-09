import random


class BlackJack():
    def dealCards(self):
        cardList = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card = random.choice(cardList)
        return card

    def calculateScore(self, cards):
        if sum(cards) == 21 and len(cards) == 2:
            return 0
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)

    def compare(self,userScore, computerScore):
        if userScore > 21 and computerScore > 21:
            return "You went over. You lose 😤"

        if userScore == computerScore:
            return "Draw 🙃"
        elif computerScore == 0:
            return "Lose, opponent has Blackjack 😱"
        elif userScore == 0:
            return "Win with a Blackjack 😎"
        elif userScore > 21:
            return "You went over. You lose 😭"
        elif computerScore > 21:
            return "Opponent went over. You win 😁"
        elif userScore > computerScore:
            return "You win 😃"
        else:
            return "You lose 😤"