import json
import urllib.request
import random
import os
from time import sleep


def cleanScreen():
    clear = lambda: os.system('cls')
    clear()


class TriviaGame:
    def __init__(self):
        with urllib.request.urlopen("https://opentdb.com/api.php?amount=10&type=multiple") as url:
            self.data = json.loads(url.read().decode())
            self.Game = len(self.data['results'])
            self.Player = ""
            self.Score = 0

    def playerSettings(self):
        print("**************************************")
        print("*     Welcome to my Trivia Game!     *")
        print("*        What is your name?          *")
        print("**************************************")
        self.Player = input()
        cleanScreen()

    def CheckingAns(self, CorrectAnswer, SelectedAns):
        if CorrectAnswer == SelectedAns:
            self.Score += 1
            return f'Well done {self.Player}, Correct answer!'
        else:
            return f'Incorrect answers {self.Player}. Maybe next time.'

    def LetsPlay(self):
        for i in range(0, self.Game):
            print(f'Question # {i + 1}')
            Question = self.data['results'][i]['question'].replace('&quot;', "'").replace('&#039;', "'")
            Category = self.data['results'][i]['category']
            print(f'Category: {Category}\n')
            print(Question + "\n")
            CorrectAnswer = self.data['results'][i]['correct_answer'].replace('&quot;', "'").replace('&#039;', "'")
            IncorrectAnswers = self.data['results'][i]['incorrect_answers']
            # print(CorrectAnswer)
            Answers = [CorrectAnswer, *IncorrectAnswers]
            random.shuffle(Answers)
            print("1. {}\t\t 2. {}\t\t 3. {}\t\t 4. {}".format(*Answers).replace('&quot;', "'").replace('&#039;', "'"))
            SelectedAns = int(input())

            while SelectedAns != 1 and SelectedAns != 2 and SelectedAns != 3 and SelectedAns != 4:
                print("Please, Choose an answer from 1 - 4")
                SelectedAns = int(input())

            print(self.CheckingAns(CorrectAnswer, Answers[SelectedAns - 1]))
            sleep(2)
            cleanScreen()
        print(
            f'Hi! {self.Player},\nThe game is over, You answered Correctly on {self.Score}'
            f' Questions,\nHope to see you soon.')


Trivia = TriviaGame()
Trivia.playerSettings()
Trivia.LetsPlay()
