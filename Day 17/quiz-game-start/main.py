from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import random

question_bank = []

# Write a for loop to iterate over the question_data.
for question in question_data:
    # Create a Question object from each entry in question_data.
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    # Append each Question object to the question_bank.
    question_bank.append(new_question)

random.shuffle(question_bank)
quiz = QuizBrain(question_bank)

# Use the while loop to show the next question until the end
while quiz.still_has_question():# if quiz still has questions remaining
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")