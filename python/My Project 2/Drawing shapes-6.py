from turtle import Turtle,Screen
window=Screen()
window.title("Drawing shapes:")

sam=Turtle()
sam.speed("fast")

def circle():
    sam.pencolor("black")
    sam.pensize(3)
    sam.shape("square")
    sam.circle(100)
    
def triangle():
    sam.pencolor("purple")
    sam.pensize(4) 
    sam.shape("circle")
    for _ in range(3):
        sam.forward(200)
        sam.left(360 / 3)
def square():
    sam.pencolor("red")
    sam.pensize(6) 
    sam.shape("turtle")
    for _ in range(4):
        sam.forward(100)
        sam.left(360 / 4)    
    
    

while True:
    user_name=window.textinput("wait a bit","what do you want to drow ? write (A/E)").lower()
    if user_name=="circle" or user_name=="دائرة":
        circle()
    elif user_name=="triangle" or user_name=="مثلث":
        triangle()
    elif user_name=="square" or user_name=="مربع":     
        square()
    elif user_name=="exit" or user_name=="خروج":
        sam.clear()   
        window.bgcolor("pink")
        sam.hideturtle()
        sam.write("Press any key to exit \n إضغط في آي مكان للخروج ",font=("arial",20,"normal"),align="center")
        window.exitonclick()
    else:
        pass
   






