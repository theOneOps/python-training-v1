import random
from data import question_data
from question_model import Question


def initialize(countgg, nbcount):
    nbcount += 1
    if question_data:
        ourchoice = random.choice(question_data)
        thequestion = Question(nbcount, ourchoice['text'], ourchoice['answer'])
        inputanswer = input(f'Q.{thequestion.id} {thequestion.question} (True/False): ')
        if inputanswer == thequestion.answer:
            countgg += 1
            question_data.remove(ourchoice)
            print("You got it right !")
            print(f'the correct answer was {thequestion.answer}.')
            print(f'Your current score is {countgg}/{nbcount}.')
            initialize(countgg, nbcount)
        else:
            print("That's wrong !")
            print(f'the correct answer was {thequestion.answer}.')
            print(f'Your current score is {countgg}/{nbcount}.')
            return False
    else:
        print("There is no question to answer again !")
        print("Congratulations")
        return False
