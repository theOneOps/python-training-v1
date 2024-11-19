from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

datas=question_data
list_data=[]
for question in datas:
    current_question=question["text"]
    correct_answer=question["answer"]
    new_question=Question(current_question,correct_answer)
    list_data.append(new_question)

quiz=QuizBrain(list_data)
def continue_game():
    while quiz.still_has_questions():
        quiz.next_question()
        print("\n")

continue_game()

