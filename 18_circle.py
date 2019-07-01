


import turtle
for i in range(1,6):
    if i%2==0:
        turtle.pencolor('red')
    else:
        turtle.pencolor('green')
    turtle.penup()
    turtle.goto(0,-50*i)
    turtle.pendown()
    turtle.circle(50*i)

