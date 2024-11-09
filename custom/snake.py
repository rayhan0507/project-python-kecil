import turtle
import random
import time

delay = 0.1
score = 0
highscore = 0


wn = turtle.Screen()
wn.title("snake game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "Stop"

food = turtle.Turtle()
colors = random.choice(["red", "green", "yellow"])
shape = random.choice(["square", "circle", "triangle"])
food.speed(0)
food.shape(shape)
food.color(colors)
food.penup()
food.goto(0,100)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("score: 0 highscore: 0", align="center", font=("candara", 24, "bold"))

def goup():
    if head.direction != "down":
        head.direction = "up"

    
def godown():
    if head.direction != "up":
        head.direction = "down"


def goright():
     if head.direction != "left":
        head.direction = "right"

    
def goleft():
     if head.direction != "right":
        head.direction = "left"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
  
wn.listen()
wn.onkeypress(goup, "w")
wn.onkeypress(godown, "s")
wn.onkeypress(goright, "d")
wn.onkeypress(goleft, "a")

segmen = []

while True:
    wn.update()
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "Stop"
        colors = random.choice(["red", "green", "yellow"])
        shape = random.choice(["square", "circle", "triangle"])
        for segment in segmen:
            segment.goto(1000, 1000)
        segmen.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("score: {} highscore: {}".format(score, highscore), align="center", font=("candara", 24, "bold"))
    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)

        new_segmen = turtle.Turtle()
        new_segmen.speed(0)
        new_segmen.shape("square")
        new_segmen.color("orange")
        new_segmen.penup()
        segmen.append(new_segmen)
        delay -= 0.001
        score += 10
        if score > highscore:
            highscore = score
        pen.clear()
        pen.write("score: {} highscore: {}".format(score, highscore), align="center", font=("candara", 24, "bold"))
    for index in range(len(segmen)-1, 0, -1):
        x = segmen[index - 1].xcor()
        y = segmen[index - 1].ycor()
        segmen[index].goto(x, y)
    if len(segmen) > 0:
        x = head.xcor()
        y = head.ycor()
        segmen[0].goto(x, y)
    move()
    for segment in segmen:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "Stop"
            colors = random.choice(["red", "green", "yellow"])
            shape = random.choice(["square", "circle", "triangle"])
            for segment in segmen:
                segment.goto(1000, 1000)
            segmen.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write("score: {} highscore: {}".format(score, highscore), align="center", font=("candara", 24, "bold"))
    time.sleep(delay)
