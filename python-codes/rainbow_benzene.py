import turtle

colors = ['red','blue','purple','green','orange','yellow']

t = turtle.Pen()
turtle.bgcolor("white")
for x in range(60):
    t.pencolor(colors[x%6])
    t.width(x/100 + 1)
    t.forward(x)
    t.left(59)

turtle.exitonclick()