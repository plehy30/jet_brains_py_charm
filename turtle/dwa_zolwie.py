import turtle

t = turtle.Turtle()
t.shape('turtle')
t.color('red')
t.pensize(7)
t.penup()
t.goto(-200, 100)
t.pendown()
t.forward(300)

t2 = turtle.Turtle()
t2.shape('turtle')
t2.color('blue')
t2.pensize(7)
t2.penup()
t2.goto(-200, -100)
t2.pendown()
t2.forward(150)
turtle.exitonclick()
