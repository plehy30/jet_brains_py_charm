import turtle

zolw = turtle.Turtle()
zolw.shape("turtle")

zolw.penup()
zolw.goto(-200, 150)
zolw.pendown()
zolw.color('green')
zolw.fillcolor('green')
zolw.begin_fill()
for i in range(3):
    zolw.forward(150)
    zolw.left(120)
zolw.end_fill()
zolw.penup()
zolw.goto(200, 150)
zolw.pendown()
zolw.color('blue')
zolw.fillcolor('blue')
zolw.begin_fill()
for i in range(3):
    zolw.forward(150)
    zolw.left(120)
zolw.end_fill()
zolw.penup()
zolw.goto(-200, -150)
zolw.pendown()
zolw.color('purple')
zolw.fillcolor('purple')
zolw.begin_fill()
for i in range(3):
    zolw.forward(150)
    zolw.left(120)
zolw.end_fill()
zolw.penup()
zolw.goto(200, -150)
zolw.pendown()
zolw.color('yellow')
zolw.fillcolor('yellow')
zolw.begin_fill()
for i in range(3):
    zolw.forward(150)
    zolw.left(120)
zolw.end_fill()
zolw.penup()
zolw.goto(-120, 300)
zolw.pendown()
zolw.color('black')
zolw.write('Mam na imię Tomek', font=("Arial", 30, "bold"))

turtle.exitonclick()
