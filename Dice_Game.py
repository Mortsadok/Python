from random import randrange
import time
import os


def cleanScreen():
    clear = lambda: os.system('cls')
    clear()


# function that return`s random number between 1-6
def returnRandom():
    return randrange(1, 7)


# game function
def DiceGame():
    tempSumP1, tempSumP2, totalSumP1, totalSumP2, maxPointsP1, maxPointsP2, i = (0, 0, 0, 0, 0, 0, 0)

    Player1 = input("Hi Player 1,\nWhat`s Your Name?\n")
    cleanScreen()

    Player2 = input("Hi Player 2,\nWhat`s Your Name?\n")
    cleanScreen()

    while totalSumP1 < 100 and totalSumP2 < 100:
        keyWord = ""
        if i % 2 == 0:
            while keyWord != "pass":
                randomCube = returnRandom()
                if randomCube == 1:
                    print("[%s, Total Points: %d]\n" % (Player1, totalSumP1))
                    print("*  *  *\n*  %d  *\n*  *  *\n" % randomCube)
                    print("%s, Try next time when your turn comes again." % Player1)
                    tempSumP1 = 0
                    keyWord = "pass"
                    time.sleep(3)
                    cleanScreen()

                else:
                    print("[%s, Total Points: %d]" % (Player1, totalSumP1))
                    print("*  *  *\n*  %d  *\n*  *  *\n" % randomCube)
                    tempSumP1 += randomCube
                    print("Round Points: %d\n" % tempSumP1)
                    keyWord = input("%s, Take the risk and roll dice Or pass turn?\n" % Player1)
                    cleanScreen()

                    if keyWord == "pass":
                        totalSumP1 += tempSumP1
                        print(totalSumP1)
                        if tempSumP1 > maxPointsP1:
                            maxPointsP1 = tempSumP1
                        tempSumP1 = 0
                        cleanScreen()
        if i % 2 != 0:
            while keyWord != "pass":
                randomCube = returnRandom()
                if randomCube == 1:
                    print("[%s, Total Points: %d]\n" % (Player2, totalSumP2))
                    print("*  *  *\n*  %d  *\n*  *  *\n" % randomCube)
                    print("%s, Try next time when your turn comes again." % Player2)
                    tempSumP2 = 0
                    keyWord = "pass"
                    time.sleep(3)
                    cleanScreen()

                else:
                    print("[%s, Total Points: %d]\n" % (Player2, totalSumP2))
                    print("*  *  *\n*  %d  *\n*  *  *\n" % randomCube)
                    tempSumP2 += randomCube
                    print("Round Points: %d\n" % tempSumP2)
                    keyWord = input("%s, Take the risk and roll dice Or pass turn?\n" % Player2)
                    cleanScreen()

                    if keyWord == "pass":
                        totalSumP2 += tempSumP2
                        print(totalSumP2)
                        if tempSumP2 > maxPointsP2:
                            maxPointsP2 = tempSumP2
                        tempSumP2 = 0
                        cleanScreen()
        i += 1
    cleanScreen()

    if totalSumP1 >= 100:
        print("Congratulations %s You Win!" % Player1)
        print("[Max points you collected per Round: %d]\n" % maxPointsP1)

    if totalSumP2 >= 100:
        print("Congratulations %s You Win!" % Player2)
        print("[Max points you collected per Round: %d]\n" % maxPointsP2)
    time.sleep(5)


# main:
DiceGame()
