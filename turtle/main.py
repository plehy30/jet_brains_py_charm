from turtle import *
import turtle

bgcolor("white")
monty = turtle.Turtle()
monty.shape('turtle')
monty.shapesize(3)

monty.speed(1)
monty.pen(pensize='10')
monty.color('red')
monty.fillcolor("blue")
monty.begin_fill()
monty.forward(100)
monty.left(90)
monty.forward(100)
monty.left(90)
monty.forward(100)
monty.left(90)
monty.forward(100)
monty.end_fill()

monty.penup()
monty.goto(-100, 100)
monty.pendown()
monty.forward(200)
monty.left(90)
monty.forward(200)
monty.left(90)
monty.forward(200)
monty.left(90)
monty.forward(200)

done()
