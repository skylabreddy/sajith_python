import turtle

# Fast input setup
screen = turtle.Screen()
screen.title("Fast Input Turtle Graphics - Circle")
screen.setup(width=800, height=600)

# Create a turtle
t = turtle.Turtle()
t.speed(0)  # Set the fastest drawing speed

# Draw a circle
t.circle(100)  # Radius of the circle is 100

# Keep the window open
screen.mainloop()

