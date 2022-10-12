import turtle

monty = turtle.Turtle()
monty.shape("turtle")

monty.penup()
monty.goto(-200, 200)
monty.write("Latający", font=("Arial", 30, "bold"))
monty.goto(-100, 100)
monty.write("Żółw", font=("Arial", 30, "bold"))
monty.goto(0, 0)
monty.write("Monty", font=("Arial", 30, "bold"))
monty.goto(100, -100)
monty.write("Pythona", font=("Arial", 30, "bold"))
monty.goto(200, -200)
monty.write("He, hej, hej", font=("Arial", 30, "bold"))
turtle.exitonclick()
