import random

def welcome(k):
    print('Welcome {} to the 8-ball machine!'.format(k))
name = input('What is your username?: ')

welcome(name)

answerList = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes, definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Cannot predict now']

def question(n):
    print(random.choice(answerList))
question_answer = input('What is your question?: ')

question(question_answer)
