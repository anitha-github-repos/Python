class QuizBrain:
    def __init__(self,question_list):
        self.question_list = question_list
        self.question_number = 0
        self.correct_answer = 0

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number +=1
        user_responce = input(f"Q.{self.question_number}: {question.text} (True/False)?: ")
        if user_responce == question.answer:
            self.correct_answer+=1
            print("You Got it right!")
            print(f"The correct answer was : {question.answer}.")
            print(f"Your current score is : {self.correct_answer}/{self.question_number}")
            print("\n")
        else:
            print("That's wrong.")
            print(f"The correct answer was : {question.answer}.")
            print(f"Your current score is : {self.correct_answer}/{self.question_number}")
            print("\n")

