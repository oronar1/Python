"""data.py: Data source for QuizMe App

A simple trivia app based on the code found in the credits.
Uses Open Trivia Database (https://opentdb.com/) as the source
of questions."""

import requests
from question_model import Question


__author__ = "Michael Bochkovski"
__copyright__ = "Copyright 2023, EMS_PI"
__credits__ = ["100 Days of Code: The Complete Python Pro Bootcamp for 2023 - Dr. Angela Yu"]
__license__ = "MIT"

QUIZ_DATA_SITE = 'https://opentdb.com/api.php'
CATEGORIES = []
CATEGORY_IDS = []
DIFFICULTY_LEVELS = [
    "Any difficulty",
    "Easy",
    "Medium",
    "Hard"
]
QUESTION_NUMS = None


def quiz_data(amount, category, difficulty):
    parameters = {
        "amount": int(amount),
        "category": category,
        "difficulty": difficulty.lower(),
        "type": "boolean"
    }
    if category == 0:
        del parameters["category"]

    if difficulty.lower() == "any difficulty":
        del parameters["difficulty"]
    question_response = requests.get(QUIZ_DATA_SITE, params=parameters)
    temp = question_response.json()
    question_data = temp["results"]
    question_bank = []
    for q in question_data:
        question_bank.append(Question(q["question"], q["correct_answer"]))
    return question_bank


def get_global_trivia_data():
    CATEGORIES.clear()
    CATEGORY_IDS.clear()
    trivia_categories_response = requests.get(QUIZ_DATA_SITE[0:19] + "/api_category.php")
    trivia_categories_response.raise_for_status()
    trivia_categories_data = trivia_categories_response.json()['trivia_categories']
    for category in range(0, len(trivia_categories_data)):
        CATEGORIES.append(trivia_categories_data[category]["name"])
        CATEGORY_IDS.append(trivia_categories_data[category]["id"])
    CATEGORIES.append("Any category")
    CATEGORY_IDS.append(0)



def get_question_num(category_id):
    trivia_categories_response = requests.get(f"https://opentdb.com/api_count.php?category={category_id}")
    trivia_categories_response.raise_for_status()
    trivia_categories_quest_num = trivia_categories_response.json()["category_question_count"]
    trivia_category_quest_num = {
        DIFFICULTY_LEVELS[0]: trivia_categories_quest_num["total_question_count"],
        DIFFICULTY_LEVELS[1]: trivia_categories_quest_num["total_easy_question_count"],
        DIFFICULTY_LEVELS[2]: trivia_categories_quest_num["total_medium_question_count"],
        DIFFICULTY_LEVELS[3]: trivia_categories_quest_num["total_hard_question_count"]
    }
    return trivia_category_quest_num

def get_response(category, difficulty,amount):
    parameters = {
        "amount": int(amount),
        "category": category,
        "difficulty": difficulty.lower(),
        "type": "boolean"
    }
    req_res=requests.get(QUIZ_DATA_SITE, params=parameters)
    return req_res.json()['response_code']

