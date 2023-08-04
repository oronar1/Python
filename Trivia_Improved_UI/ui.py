"""ui.py: Main GUI for QuizMe App

A simple trivia app based on the code found in the credits.
Uses Open Trivia Database (https://opentdb.com/) as the source
of questions."""

import tkinter as tk
from quiz_brain import QuizBrain
from setup import SetupUI
from tkinter import messagebox

__author__ = "Michael Bochkovski"
__copyright__ = "Copyright 2023, EMS_PI"
__credits__ = ["100 Days of Code: The Complete Python Pro Bootcamp for 2023 - Dr. Angela Yu"]
__license__ = "MIT"

THEME_COLOR = "#375362"


def do_nothing():
    pass


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.feedback = []

        self.window = tk.Tk()
        self.window.title("QuizMe")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        menubar = tk.Menu(self.window)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="New...", command=self.setup_ui)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.on_closing)
        menubar.add_cascade(label="File", menu=file_menu)

        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="Help Index", command=do_nothing)
        help_menu.add_command(label="About...", command=do_nothing)
        menubar.add_cascade(label="Help", menu=help_menu)
        self.window.config(menu=menubar)

        self.question_count_label = tk.Label(text=f"Question 1/{self.quiz.num_questions}",
                                             bg=THEME_COLOR, fg="white", justify="center")
        self.question_count_label.grid(row=0,
                                       column=0,
                                       padx=20,
                                       pady=(0, 20)
                                       )

        self.score_label = tk.Label(text="Score: 0",
                                    bg=THEME_COLOR,
                                    fg="white",
                                    justify="center")
        self.score_label.grid(row=0,
                              column=1,
                              padx=20,
                              pady=(0, 20)
                              )

        self.canvas = tk.Canvas(width=300, height=250)
        self.canvas.grid(row=1, column=0, columnspan=2)
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="Quiz question is coming",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 18, "italic"),
                                                     width=280)

        true_img = tk.PhotoImage(file="./images/true.png")
        self.true_button = tk.Button(image=true_img,
                                     borderwidth=0,
                                     highlightthickness=0,
                                     command=self.answer_true
                                     )
        self.true_button.grid(row=2, column=0, padx=20, pady=(20, 0))

        false_img = tk.PhotoImage(file="./images/false.png")
        self.false_button = tk.Button(image=false_img,
                                      borderwidth=0,
                                      highlightthickness=0,
                                      command=self.answer_false)
        self.false_button.grid(row=2, column=1, padx=20, pady=(20, 0))

        self.next_question()

        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.window.mainloop()

    def next_question(self):
        if self.feedback:
            self.canvas.delete(self.feedback)
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            question = self.quiz.next_question()
            self.true_button.config(state="normal")
            self.false_button.config(state="normal")
        else:
            question = "You have reached the end of the quiz!"
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
        self.canvas.itemconfig(self.question_text, text=question)
        self.score_label.config(text=f"Score : {self.quiz.score}")
        self.question_count_label.config(text=f"Question {self.quiz.question_number}/{self.quiz.num_questions}")

    def answer_true(self):
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
        check_result = self.quiz.check_answer("True")
        self.answer_feedback(check_result)

    def answer_false(self):
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
        check_result = self.quiz.check_answer("False")
        self.answer_feedback(check_result)

    def answer_feedback(self, check_result):
        if check_result:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.next_question)

    def setup_ui(self):
        params = {
            "category": self.quiz.category,
            "difficulty": self.quiz.difficulty,
            "num_questions": self.quiz.num_questions
        }
        SetupUI(self, params)

    def setup_quiz(self, category, difficulty, num_questions):
        params = {
            "category": category,
            "difficulty": difficulty,
            "amount": num_questions
        }
        self.quiz.setup(params)
        self.next_question()

    def on_closing(self):
        if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.window.destroy()




