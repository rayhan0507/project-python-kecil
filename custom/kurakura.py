from turtle import *
from random import randint


speed(10)
penup()
goto(-200,200)

for step in range(20):
   write(step, align="center")
   right(90)
   for line in range(10):
      penup()
      forward(10)
      pendown()
      forward(10)
   penup()
   backward(200)
   left(90)
   forward(20)


rosie = Turtle()
rosie.color("red")
rosie.shape("turtle")

rosie.penup()
rosie.goto(-220, 160)
rosie.pendown()

for turn in range(10):
   rosie.right(36)

b = Turtle()
b.color("black")
b.shape("circle")

b.penup()
b.goto(-220, 120)
b.pendown()

for turn in range(10):
   b.right(36)

c = Turtle()
c.color("green")
c.shape("square")

c.penup()
c.goto(-220, 80)
c.pendown()

for turn in range(10):
   c.right(36)

d = Turtle()
d.color("yellow")
d.shape("triangle")

d.penup()
d.goto(-220, 40)
d.pendown()

for turn in range(10):
   d.right(36)

for turn in range(150):
   rosie.forward(randint(1, 5))
   b.forward(randint(1, 5))
   c.forward(randint(1, 5))
   d.forward(randint(1, 5))