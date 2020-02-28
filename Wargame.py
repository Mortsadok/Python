from random import randint


class WarGame:
    def __init__(self):
        self.Cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
        self.Dict = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    # random cards for each player
    def getCards(self, Hand):
        for i in range(0, 5):
            Hand.append(self.Cards[randint(0, 13)])

    # change the value of the card whose value is greater than 10: ('J', 'Q', 'K', 'A')
    def ChangeValues(self, Hand):
        for i in range(0, len(Hand)):
            for j in self.Dict.keys():
                if Hand[i] == j:
                    Hand[i] = self.Dict.get(j)

    @staticmethod
    def whoWin(Player1, Player2):
        countP1, countP2 = (0, 0)
        for i in range(0, len(Player1)):
            if Player1[i] > Player2[i]:
                countP1 += 1
            if Player2[i] > Player1[i]:
                countP2 += 1

        if countP1 > countP2:
            return "Player 1 Wins!\n"

        if countP2 > countP1:
            return "Player 2 Wins!\n"

        elif countP1 == countP2:
            return "Its a Tie!"


WarGame = WarGame()
Players = PlayerOne, PlayerTwo = ([], [])

for i in Players:
    WarGame.getCards(i)
    WarGame.ChangeValues(i)

print(WarGame.whoWin(PlayerOne, PlayerTwo))
