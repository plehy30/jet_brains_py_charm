import turtle

monty = turtle.Turtle()
monty.shape("turtle")

monty.fillcolor('blue')
monty.begin_fill()
monty.forward(100)
monty.left(90)
monty.forward(100)
monty.left(90)
monty.forward(100)
monty.left(90)
monty.forward(100)
monty.left(90)
monty.end_fill()

monty.goto(50, 100)
turtle.exitonclick()
