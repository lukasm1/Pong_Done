from turtle import Turtle

X = 0
Y = 250
FONT = ("Courier", 50, "bold")
ALIGNMENT = "center"


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.user_score = 0
        self.pc_score = 0
        self.hideturtle()
        self.color("white")
        self.goto(X, Y)
        self.write(arg=f"{self.user_score}     {self.pc_score}", align=ALIGNMENT, font=FONT)
        self.create_line()

    def pc_point(self):
        self.pc_score += 1
        self.update_score()

    def user_point(self):
        self.user_score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.create_line()
        self.goto(X, Y)
        self.write(arg=f"{self.user_score}     {self.pc_score}", align=ALIGNMENT, font=FONT)

    def create_line(self):
        self.goto(0, -300)
        self.setheading(90)
        self.pensize(5)
        for _ in range(30):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(20)
