import turtle

monty = turtle.Turtle()
monty.shape("turtle")

monty.fillcolor('blue')
monty.penup()
monty.goto(-200, -200)
monty.pendown()
monty.begin_fill()
monty.color('blue')
for i in range(4):
    monty.forward(100)
    monty.right(90)
monty.goto(-100, -200)
for i in range(4):
    monty.forward(100)
    monty.right(90)
monty.goto(0, -200)
for i in range(4):
    monty.forward(100)
    monty.right(90)
monty.goto(100, -200)
for i in range(4):
    monty.forward(100)
    monty.right(90)
monty.goto(200, -200)
for i in range(4):
    monty.forward(100)
    monty.right(90)
monty.end_fill()
monty.penup()
monty.goto(-200, -100)
monty.pendown()
monty.begin_fill()
for i in range(4):
    monty.forward(100)
    monty.right(90)
monty.end_fill()
monty.penup()
monty.goto(0, -100)
monty.pendown()
monty.begin_fill()
for i in range(4):
    monty.forward(100)
    monty.right(90)
monty.end_fill()
monty.penup()
monty.goto(200, -100)
monty.pendown()
monty.begin_fill()
for i in range(4):
    monty.forward(100)
    monty.right(90)
monty.end_fill()
monty.penup()
monty.goto(-200, -100)
monty.pendown()
monty.begin_fill()
for i in range(3):
    monty.forward(100)
    monty.left(120)
monty.penup()
monty.goto(0, -100)
monty.pendown()
for i in range(3):
    monty.forward(100)
    monty.left(120)
monty.penup()
monty.goto(200, -100)
monty.pendown()
for i in range(3):
    monty.forward(100)
    monty.left(120)
monty.end_fill()
monty.penup()
monty.goto(-120, 100)
monty.pendown()
monty.color('black')
monty.write('ZROBIONE', font=("Arial", 30, "bold"))

turtle.exitonclick()