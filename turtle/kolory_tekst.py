import turtle

turtle.bgcolor('black')
t = turtle.Turtle()
t.shape('turtle')
t.color('red')
t.circle(50)
t.penup()
t.goto(-200, 0)
t.pendown()
t.color('white')
t.write('Cześć', font=("Arial", 30, "bold"))
t.hideturtle()
turtle.exitonclick()
