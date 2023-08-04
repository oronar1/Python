"""ui.py: Question model for QuizMe App

A simple trivia app based on the code found in the credits.
Uses Open Trivia Database (https://opentdb.com/) as the source
of questions."""

__author__ = "Ethem M Sözer"
__copyright__ = "Copyright 2023, EMS_PI"
__credits__ = ["100 Days of Code: The Complete Python Pro Bootcamp for 2023 - Dr. Angela Yu"]
__license__ = "MIT"


class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
