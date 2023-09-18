import turtle
import time

s = turtle.getscreen()
t1 = turtle.Turtle()
t2 = turtle.Turtle()

turtles = [t1,t2]

x = 30
t1.right(x)
t2.right(-1*x)
for i in turtles: i.forward(100)

x = 50
t1.left(x)
t2.left(-1*x)

t1.forward(50)
t2.forward(50)

time.sleep(3)