class QuizBrain:
    def __init__(self,question_list):
        self.question_number=0
        self.correct_answer=0
        self.question_list=question_list

    def still_has_questions(self):
        if self.question_number > len(self.question_list)-1:
            print("you've completed the quiz")
            print(f"Your final score is {self.correct_answer}/{self.question_number}")
            return False
        else:
            return True

    def next_question(self):
        if self.question_number > len(self.question_list):
            return
        question=self.question_list[self.question_number]
        self.question_number+=1
        player_answer=input(f"Q.{self.question_number}: {question.text}. (True/false) ? ")
        if player_answer == question.answer:
            self.correct_answer+=1
            print("You got it right")
            print(f"the correct answer was :{question.answer}")
            print(f"Your current score is : {self.correct_answer}/{self.question_number}")
        else:
            print("that's wrong")
            print(f"the correct answer was :{question.answer}")
            print(f"Your current score is : {self.correct_answer}/{self.question_number}")









