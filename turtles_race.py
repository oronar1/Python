from turtle import Turtle, Screen
import random

is_race_on = False
tim = Turtle()
screen = Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make youir bet",prompt="Which turtle will win the race? Enter a color: ")
colors=["red","orange","yellow","green","blue","purple"]
#speeds=[1,3,5,2,4]
turtles=[]

for i in range(5):
    constY=i*30
    tim=Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-240,y=-100+constY)
    #tim.speed(random.choice(speeds))
    turtles.append(tim)

if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor()>230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won!")
            else:
                print(f"You have lost, {winning_color} turtle has won! ")
                
        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)
        

screen.exitonclick()
