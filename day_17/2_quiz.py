question_data = [
    {"text": "is cockroach blood red?",
     "answer": "False"},
    {"text": "the color of octupus is black.",
     "answer": "true"},
]


class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer


# call the function now
#new_q = Question("hgsh", "false")
# print(new_q.text)
question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(
            f"Q.{self.question_number}: {current_question.text}. (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("you got it right!")

        else:
            print("it's wrong.")
        print(f"the correct answer was:{correct_answer}.")
        print(f"ypor current score is: {self.score}/{self.question_number}.")
        print("\n")


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print("you have completed the quiz.")
print(f"your final score is: {quiz.score}/{quiz.question_number}.")
