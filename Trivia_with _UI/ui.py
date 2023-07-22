from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     text="some text",
                                                     width=280,
                                                     fill=THEME_COLOR,
                                                     font=("Ariel", 20, "italic")
                                                     )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.lbl_score = Label(self.window, text=f"Score: 0", fg="white", width=20, pady=20, font=("ariel", 10),
                               bg=THEME_COLOR, highlightthickness=0)
        self.lbl_score.grid(column=1, row=0)

        false_image = PhotoImage(file="images/false.png")
        true_image = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=true_image, highlightthickness=0, pady=20, padx=10, command=self.true_pressed)
        self.false_btn = Button(image=false_image, highlightthickness=0, pady=20, padx=10, command=self.false_pressed)
        self.true_btn.grid(column=1, row=2)
        self.false_btn.grid(column=0, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.lbl_score.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.question_text,text="You've reached the end of the Quiz")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
