import turtle

# Setup turtle screen
screen = turtle.Screen()
screen.bgcolor("skyblue")
screen.title("Shizuka Minamoto")

shizu = turtle.Turtle()
shizu.speed(6)
shizu.pensize(2)

def draw_circle(color, x, y, radius):
    shizu.penup()
    shizu.goto(x, y - radius)
    shizu.pendown()
    shizu.color(color)
    shizu.begin_fill()
    shizu.circle(radius)
    shizu.end_fill()

# Face
draw_circle("peachpuff", 0, 100, 60)

# Eyes
draw_circle("white", -20, 130, 10)
draw_circle("white", 20, 130, 10)
draw_circle("black", -20, 130, 3)
draw_circle("black", 20, 130, 3)

# Smile
shizu.penup()
shizu.goto(-20, 80)
shizu.setheading(-60)
shizu.color("black")
shizu.pendown()
shizu.circle(20, 120)

# Hair top
shizu.penup()
shizu.goto(-60, 160)
shizu.setheading(60)
shizu.color("black")
shizu.pensize(4)
shizu.pendown()
shizu.circle(70, 60)

# Side hair
shizu.penup()
shizu.goto(-50, 140)
shizu.setheading(210)
shizu.pendown()
shizu.circle(25, 90)

shizu.penup()
shizu.goto(50, 140)
shizu.setheading(-30)
shizu.pendown()
shizu.circle(25, 90)

# Body (dress)
shizu.penup()
shizu.goto(-40, 40)
shizu.setheading(0)
shizu.color("hotpink")
shizu.pendown()
shizu.begin_fill()
for _ in range(2):
    shizu.forward(80)
    shizu.right(90)
    shizu.forward(100)
    shizu.right(90)
shizu.end_fill()

#
