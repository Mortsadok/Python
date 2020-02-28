import datetime
from time import sleep
import os


def cleanScreen():
    clear = lambda: os.system('cls')
    clear()


class ChatBot:
    def __init__(self):
        self.BotQuestions = {
            'How are you?': 'I am good Thank you!', "What is your name?": "My name is: AI Bot.",
            "What is the time now?": f'{datetime.datetime.now().time()}'[:5],
            "What is the Date today?": f'{datetime.datetime.now().date()}'
        }

    def BotAnswers(self, Question):
        for Ask in self.BotQuestions.keys():
            if Ask == Question:
                Answer = self.BotQuestions.get(Ask)
                print(Answer)


Bot = ChatBot()
BotStatus = True
while BotStatus:
    Question = input("Hi,\nI am a chat bot, How can i help you?\n")
    Bot.BotAnswers(Question)
    sleep(2)
    cleanScreen()
