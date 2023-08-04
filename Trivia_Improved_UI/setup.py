"""ui.py: Setup for QuizMe App

A simple trivia app based on the code found in the credits.
Uses Open Trivia Database (https://opentdb.com/) as the source
of questions."""

import tkinter as tk
from tkinter import messagebox

import requests
import data
import ui

__author__ = "Michael Bochkovsky"
__copyright__ = "Copyright 2023, EMS_PI"
__credits__ = ["100 Days of Code: The Complete Python Pro Bootcamp for 2023 - Dr. Angela Yu"]
__license__ = "MIT"

THEME_COLOR = "#375362"

CATEGORIES = data.CATEGORIES

CATEGORY_IDS = data.CATEGORY_IDS

DIFFICULTY_LEVELS = data.DIFFICULTY_LEVELS


class SetupUI:
    def __init__(self, main_ui, selected_params):
        self.main_ui = main_ui

        self.window = tk.Toplevel()
        self.window.title("QuizMe: Setup")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        data.get_global_trivia_data()

        # category configurations
        category_label = tk.Label(self.window,
                                  text="Category:",
                                  anchor='e',
                                  justify='left',
                                  bg=THEME_COLOR,
                                  fg="white")
        category_label.grid(row=0, column=0, sticky="W", padx=5, pady=5)
        self.category = tk.StringVar()
        self.category.set(CATEGORIES[CATEGORY_IDS.index(selected_params["category"])])
        self.category_dropdown = tk.OptionMenu(self.window, self.category, *CATEGORIES)
        self.category_dropdown.config(width=20,
                                      bg=THEME_COLOR,
                                      fg="white",
                                      highlightthickness=0)
        self.category_dropdown.grid(row=0, column=1, padx=5, pady=5, sticky="EW")

        # difficulty level configurations
        difficulty_label = tk.Label(self.window,
                                    text="Difficulty:",
                                    anchor='e',
                                    justify='left',
                                    bg=THEME_COLOR,
                                    fg="white")
        difficulty_label.grid(row=1,
                              column=0,
                              sticky="W",
                              padx=5, pady=5)
        self.difficulty = tk.StringVar()
        self.difficulty.set(selected_params["difficulty"].capitalize())
        self.difficulty_dropdown = tk.OptionMenu(self.window, self.difficulty, *DIFFICULTY_LEVELS)
        self.difficulty_dropdown.config(bg=THEME_COLOR, fg="white", highlightthickness=0)
        self.difficulty_dropdown.grid(row=1, column=1, sticky="EW", padx=5, pady=5)

        # number of questions
        num_questions_label = tk.Label(self.window, text="Number of questions:", anchor='e',
                                       justify='left', bg=THEME_COLOR, fg="white")
        num_questions_label.grid(row=2, column=0, sticky="W", padx=5, pady=5)
        self.num_questions_edit = tk.Entry(self.window)
        self.num_questions_edit.config(width=26, bg=THEME_COLOR, fg="white")
        self.num_questions_edit.insert(0, selected_params["num_questions"])
        self.num_questions_edit.grid(row=2, column=1, sticky="EW", padx=5, pady=5)

        # buttons
        self.ok_button = tk.Button(self.window, text="OK", command=self.pass_selections)
        self.ok_button.config(width=22, bg=THEME_COLOR, fg="white")
        self.ok_button.grid(row=3, column=1, sticky="EW", padx=5, pady=5)

        self.cancel_button = tk.Button(self.window, text="Cancel", command=self.cancel)
        self.cancel_button.config(width=22, bg=THEME_COLOR, fg="white")
        self.cancel_button.grid(row=3, column=0, sticky="EW", padx=5, pady=5)

        self.window.mainloop()

    def pass_selections(self):
        category = self.category.get()
        category_id = CATEGORY_IDS[CATEGORIES.index(category)]
        difficulty = self.difficulty.get()
        num_questions = self.num_questions_edit.get()

        if category_id != 0:
            if int(num_questions) > int(data.get_question_num(category_id)[difficulty]):
                num_questions=int(data.get_question_num(category_id)[difficulty])
                if num_questions > 50:
                    num_questions = 50
            elif int(num_questions) == 0:
                num_questions = 1
            else:
                pass
        else:
            num_questions = 50

        if int(data.get_response(category_id, difficulty, num_questions)) == 0:
            self.main_ui.setup_quiz(category_id, difficulty, num_questions)
        else:
            messagebox.showinfo("Information","Trivia Data Base data is insufficient.\n\tPlease correct the parameters!")

        self.window.destroy()

    def cancel(self):
        self.window.destroy()
