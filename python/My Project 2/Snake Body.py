from turtle import Turtle, Screen
import random
import time

window=Screen()
window.setup(width=800,height=500)
window.bgcolor("black")
window.tracer(0)
x_coordinate=[-40,-20,0,20,40,60,80]
angles=[90,0,0,0]
turtles=[]

#! to stope the trace 

for i in range(len(x_coordinate)):
    new_turtle=Turtle(shape="square")
    new_turtle.color("white")
    new_turtle.penup()
    new_turtle.goto(x=x_coordinate[i],y=0)
    turtles.append(new_turtle)
 

game_on=True
while game_on:
    for i in range(len(turtles)-1):
      turtles[i].goto(turtles[i+1].pos())
    turtles[-1].forward(20)
    turtles[-1].left(random.choice(angles))
    window.update()
    time.sleep(0.1)
  


window.exitonclick()

# print(len(["a","b"]))  the input is goaan be 2
print(lskf
      )