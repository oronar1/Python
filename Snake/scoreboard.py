from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial",24,"normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.score=0
        self.color("white")
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()


    def increase_score(self):
        self.score+=1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align=ALIGNMENT,font=FONT)
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", False,align=ALIGNMENT, font=FONT)
