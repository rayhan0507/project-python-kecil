import time
from turtle import *

warna = {
    'space': '#060608',
    'deepsy': '#226363',
    'coolcyan': '#4feef6',
    'perfectpurple': '#6820b0'
}

screen = Screen()
screen.setup(400, 400)
screen.bgcolor(warna['space'])

penup()
goto(0, 100)
color(warna['deepsy'])
style = ('Arial', 40, 'bold')
write('HELLO', font=style, align="center")
right(90)
forward(60)
color(warna['coolcyan'])
style = ('Arial', 40, 'bold')
write('WORLD', font=style, align="center")

hideturtle()
time.sleep(3)
goto(0,0)
color(warna['perfectpurple'])
dot(350)
