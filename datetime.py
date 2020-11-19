datetime.py

#Datetime practice


import datetime

dir(datetime)

datetime.datetime(2014, 10, 15, 10, 23, 0, 23940)


class Question:
    answer = None 
    text = None

class Add(Question):
    def __init__(self, num1 , num2)
        self.text = '{} + {}'.format(num1,num2)
        self.answer = num1 + num2

class Multiply(Question)
    def __init__(self, num1 , num2)
        self.text = '{} * {}'.format(num1,num2)
        self.answer = num1 * num2


from questions import Add, Multiply

import datetime
import random

class Quiz:
    questions = []
    answers=[]

    def __init__(self):

    def take_quiz(self):
        #log the start time
        # # # #Ask 

    def ask(self, question):
        correct = False
        question_start = datetime.datetime.now()

        answer = input(question.text + ' = ')

        if asnwer == str(question.answer)
            correct = True

        question_end = datetime.datetime.now()
        

        return correct , question_end - question_start

    def total_correct(self)
        total = 0
        for answer in self.answers:
        if answer[0]:
            total += 1
        return total

    def summary(self)
        print("You got {} out of {} right.".format(
            self.total_correct(), len(self.questions)
        ))