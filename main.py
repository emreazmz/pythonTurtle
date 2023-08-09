import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("white")
turtle_screen.title("paint")
turtle_screen.setup(width=800, height=800)

turtle_draw = turtle.Turtle()
turtle_draw.color("red")

def turtle_forward():
    turtle_draw.forward(10)

def turtle_back():
    turtle_draw.back(10)

def turtle_right():
    turtle_draw.right(5)

def turtle_left():
    turtle_draw.left(5)

def turtle_clear():
    turtle_draw.clear()

def turtle_uppen():
    turtle_draw.penup()

def turtle_pendown():
    turtle_draw.pendown()


def turtle_home():
    turtle_draw.penup()
    turtle_draw.home()
    turtle_draw.pendown()



turtle_screen.listen()
turtle_screen.onkey(fun=turtle_forward, key= "w")
turtle_screen.onkey(fun=turtle_back, key= "s")
turtle_screen.onkey(fun=turtle_right, key= "d")
turtle_screen.onkey(fun=turtle_left, key= "a")
turtle_screen.onkey(fun=turtle_uppen, key= "z")
turtle_screen.onkey(fun=turtle_pendown, key= "x")
turtle_screen.onkey(fun=turtle_clear, key= "space")
turtle_screen.onkey(fun=turtle_home, key= "h")







turtle.mainloop()