import turtle

turtle.bgcolor('black')
t = turtle.Turtle()
t.shape('turtle')
t.color('red')
for i in range(5):
    t.forward(150)
    t.right(72)
t.penup()
t.goto(-150, 50)
t.pendown()
t.color('white')
t.write('Ten program napisał Tomek', font=("Arial", 30, "bold"))
t.hideturtle()
turtle.exitonclick()
