"""main.py: Entry file for QuizMe App

A simple trivia app based on the code found in the credits.
Uses Open Trivia Database (https://opentdb.com/) as the source
of questions."""

from quiz_brain import QuizBrain
from ui import QuizInterface

__author__ = "Michael Bochkovski"
__copyright__ = "Copyright 2023, EMS_PI"
__credits__ = ["100 Days of Code: The Complete Python Pro Bootcamp for 2023 - Dr. Angela Yu"]
__license__ = "MIT"

quiz = QuizBrain()
quiz_ui = QuizInterface(quiz)
