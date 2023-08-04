"""quiz_brain.py: Quiz brain for QuizMe App

A simple trivia app based on the code found in the credits.
Uses Open Trivia Database (https://opentdb.com/) as the source
of questions."""

import html
from data import quiz_data

__author__ = "Michael Bochkovski"
__copyright__ = "Copyright 2023, EMS_PI"
__credits__ = ["100 Days of Code: The Complete Python Pro Bootcamp for 2023 - Dr. Angela Yu"]
__license__ = "MIT"

AMOUNT = 10
CATEGORY = 0
DIFFICULTY = "easy"


class QuizBrain:

    def __init__(self):
        self.question_list = None
        self.question_number = None
        self.score = None
        self.category = CATEGORY
        self.difficulty = DIFFICULTY
        self.num_questions = AMOUNT
        params = {
            "category": self.category,
            "difficulty": self.difficulty,
            "amount": self.num_questions
        }
        self.setup(params)

    def setup(self, params):
        self.category = params["category"]
        self.difficulty = params["difficulty"]
        self.num_questions = params["amount"]
        self.question_list = quiz_data(self.num_questions, self.category, self.difficulty)
        self.num_questions=len(self.question_list)
        self.score = 0
        self.question_number = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        question = self.question_list[self.question_number]
        question_text = html.unescape(question.text)
        self.question_number += 1
        return f'Q.{self.question_number}: {question_text} (True/False)?'

    def check_answer(self, u_answer):
        correct_answer = self.question_list[self.question_number-1].answer
        if correct_answer.lower() == u_answer.lower():
            self.score += 1
            return True
        else:
            return False