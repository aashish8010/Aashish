import turtle

# Setup screen
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("Shizuka Drawing")

# Turtle for drawing
shizu = turtle.Turtle()
shizu.speed(0)
shizu.pensize(2)

# Helper function: draw circle with position
def draw_circle(color, x, y, radius):
    shizu.penup()
    shizu.goto(x, y - radius)
    shizu.pendown()
    shizu.color(color)
    shizu.begin_fill()
    shizu.circle(radius)
    shizu.end_fill()

# Draw face
draw_circle("peachpuff", 0, 0, 80)

# Draw eyes
draw_circle("white", -30, 40, 15)
draw_circle("white", 30, 40, 15)
draw_circle("black", -30, 40, 5)
draw_circle("black", 30, 40, 5)

# Draw mouth
shizu.penup()
shizu.goto(-20, -20)
shizu.setheading(-60)
shizu.pendown()
shizu.circle(20, 120)

# Hair (top arc)
shizu.penup()
shizu.goto(-80, 40)
shizu.setheading(60)
shizu.color("black")
shizu.pensize(4)
shizu.pendown()
shizu.circle(90, 60)

# Hair strands (sides)
shizu.penup()
shizu.goto(-60, 60)
shizu.setheading(210)
shizu.pendown()
shizu.circle(30, 90)

shizu.penup()
shizu.goto(60, 60)
shizu.setheading(-30)
shizu.pendown()
shizu.circle(30, 90)

# Draw body (dress)
shizu.penup()
shizu.goto(-50, -80)
shizu.setheading(0)
shizu.color("hotpink")
shizu.pendown()
shizu.begin_fill()
for _ in range(2):
    shizu.forward(100)
    shizu.right(90)
    shizu.forward(120)
    shizu.right(90)
shizu.end_fill()

# Arms
shizu.penup()
shizu.goto(-50, -80)
shizu.setheading(180)
shizu.pendown()
shizu.forward(40)

shizu.penup()
shizu.goto(50, -80)
shizu.setheading(0)
shizu.pendown()
shizu.forward(40)

# Legs
shizu.penup()
shizu.goto(-30, -200)
shizu.setheading(-90)
shizu.color("peachpuff")
shizu.pendown()
shizu.forward(30)

shizu.penup()
shizu.goto(30, -200)
shizu.pendown()
shizu.forward(30)

# Hide turtle and finish
shizu.hideturtle()
turtle.done()
