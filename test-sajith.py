import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Simple Face Drawing")

# Create the turtle
pen = turtle.Turtle()
pen.speed(5)

# Draw the face (circle)
pen.penup()
pen.goto(0, -100)
pen.pendown()
pen.begin_fill()
pen.color("peachpuff")
pen.circle(100)
pen.end_fill()

# Draw the left eye
pen.penup()
pen.goto(-35, 50)
pen.pendown()
pen.begin_fill()
pen.color("white")
pen.circle(15)
pen.end_fill()

pen.penup()
pen.goto(-35, 55)
pen.pendown()
pen.begin_fill()
pen.color("black")
pen.circle(7)
pen.end_fill()

# Draw the right eye
pen.penup()
pen.goto(35, 50)
pen.pendown()
pen.begin_fill()
pen.color("white")
pen.circle(15)
pen.end_fill()

pen.penup()
pen.goto(35, 55)
pen.pendown()
pen.begin_fill()
pen.color("black")
pen.circle(7)
pen.end_fill()

# Draw the nose
pen.penup()
pen.goto(0, 30)
pen.pendown()
pen.width(3)
pen.goto(-10, 10)
pen.goto(10, 10)
pen.goto(0, 30)

# Draw the mouth
pen.penup()
pen.goto(-40, -20)
pen.setheading(-60)
pen.width(2)
pen.pendown()
pen.circle(50, 120)

# Hide the turtle
pen.hideturtle()

# Keep the window open
screen.mainloop()