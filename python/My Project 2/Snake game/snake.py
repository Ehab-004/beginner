class Snake():
    def __init__(self):
        self.x_coordinate=[-40,-20,0,20,40,60,80]
        self.turtles=[]
        self.create_sanke()
    def create_(self):
        for i in range(len(self.x_coordinate)) :
            new_turtle=tuple(shape=("square"))
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(x=self.x_coordinate[i],y=0)
            self.turtles.append(new_turtle)

    def move_snake(self):
                