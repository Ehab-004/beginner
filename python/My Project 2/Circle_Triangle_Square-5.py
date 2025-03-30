from turtle import Turtle,Screen
window=Screen()
window.bgcolor("black")
window.setup(width=1000,height=1000) #! to contol the screen dimensions

sam=Turtle()
sam.color("white")
sam.shape("turtle")
sam.speed("fastest")
sam.pensize(2)
sam.pencolor("yellow")

def drow_circle():
   sam.penup()
   sam.goto(-350,-300) #! to go to anywhere on the screen
   sam.pendown() 
   for _ in range(20):
      sam.circle(50) 
      sam.left(360 / 20)      
def drow_square():
   
   sam.penup()
   sam.goto(0,0)
   for _ in range(20):
      sam.pendown()
      for _ in range(4):
         sam.forward(70)
         sam.left(90) 
      sam.left(360 / 20)   
def drow_triangle():
   
   sam.penup()
   sam.goto(350,300)
   sam.pendown()
   for _ in range(20):
      for _ in range(3):
         sam.forward(90)
         sam.left(360 / 3)
      sam.left(360 / 20)           

drow_circle()
drow_square()
drow_triangle()









window.exitonclick()