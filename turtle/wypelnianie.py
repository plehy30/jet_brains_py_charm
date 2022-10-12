import turtle

turtle.bgcolor('black')

t = turtle.Turtle()

t.shape('turtle')
t.color('red')

t.begin_fill()

t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)

t.end_fill()

turtle.exitonclick()
