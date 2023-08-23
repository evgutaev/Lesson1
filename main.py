import turtle
import  time
t = turtle.Pen()
catokvodrat = 50 * 2
ygol = 90
t.color('dark magenta')
t.pensize(3)
#поднимаем черепашку
t.penup()
t.goto(0,200)
t.pendown()
t.left(ygol * 2)
t.forward(catokvodrat)
t.left(ygol)
t.forward(catokvodrat * 2)
t.left(ygol)
t.forward(catokvodrat)
t.left(ygol)
t.forward(catokvodrat)
t.left(ygol)
t.forward(catokvodrat)
t.color('red')
t.circle(catokvodrat / 2)
t.fillcolor("green")

t.begin_fill()
t.left(45)
t.forward(25)
t.end_fill()
time.sleep(5)