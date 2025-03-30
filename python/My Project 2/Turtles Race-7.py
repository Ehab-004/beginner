# My Teacher's project

from turtle import Turtle , Screen
import random
window=Screen()
window.title("Octocode Turtle Race")
window.setup(width=800 ,height=400)
colors=("red","green","blue")
T_positions=(-70,0,70)
Turtles=[]
user_choice=window.textinput(title="Juess whice turtle will win:",prompt="the red or the blue or the green one")


for i in range(3):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(-380,y=T_positions[i])
    Turtles.append(new_turtle)
    
def race_turtles():
    is_race_on=True
    while is_race_on:
        for turtle in Turtles:
            if turtle.xcor()  > 280:
                is_race_on=False
                winning_color=turtle.pencolor() 
                display_result(winning_color.lower()==user_choice.lower) #! it will return True or False
            else: 
              turtle.forward(random.randint(5,10))

def display_result(is_on):
    result_turtle=Turtle()
    result_turtle.hideturtle()
    result_turtle.goto(0,0)
    result_turtle.pendown()
    
    if is_on: 
        window.bgcolor("dark green")
        result_turtle.color("white")
        result_turtle.write('You win', align="center",font=("Arial",20,"normal"))
    else:
        window.bgcolor("medium violet red")
        result_turtle.color("white")   
        result_turtle.write('You Lose!', align="center",font=("Arial",20,"normal"))
        
        
race_turtles()


window.exitonclick()





 #! this is my project
# from turtle import Turtle,Screen
# import random
# window=Screen()
# window.setup(width=800,height=500)
# window.title("                     Turtles Race")

# while True:
#  user_choice=window.textinput("choic who will be the wineer:","Red Turtle or Blue Turtle or Green Turtle").lower()
#  if user_choice in ("red","green","blue"):
#     break

# #! the Turtles
# white=Turtle()  # ?? I need it to write the solution
# white.hideturtle() 
# white.pencolor("white")

# red=Turtle()
# red.shape("turtle")
# red.color("red")
# red.penup()
# red.goto(-380,-100)

# green=Turtle()
# green.shape("turtle")
# green.color("green")
# green.penup()
# green.goto(-380,100)

# blue=Turtle()
# blue.shape("turtle")
# blue.color("blue")
# blue.penup()
# blue.goto(-380,0)


# for _ in range(500):
#     red.forward(random.choice((5,10,15)))
#     blue.forward(random.choice((5,10,15)))
#     green.forward(random.choice((5,10,15)))
#     if red.xcor() >=350 or blue.xcor() >=350 or green.xcor()>=350:
#         break

# window.bgcolor("pink")

# if user_choice=="red" and red.xcor() >=blue.xcor() and red.xcor() >=green.xcor():
#     white.write("You Win ",font=("arial",30,"normal"),align="center")
 
        
# elif user_choice=="bule" and blue.xcor() >=red.xcor() and blue.xcor() >=green.xcor():
#     white.write("You Win ",font=("arial",30,"normal"),align="center") 
    
# elif user_choice=="green" and green.xcor() >=blue.xcor() and green.xcor() >=red.xcor():
#     white.write("You Win ",font=("arial",30,"normal"),align="center")
    
# else:
#     white.write("You lost ",font=("arial",30,"normal"),align="center")

# window.exitonclick()

# tutle.color() we can get to color the color of the shape and the color inside the shape
