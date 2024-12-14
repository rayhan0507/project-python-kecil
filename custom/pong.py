import turtle
import winsound


wn = turtle.Screen()
wn.title('pong game by rehan')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('blue')
paddle_a.penup()
paddle_a.goto(-350,0)
paddle_a.shapesize(5,1)

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('red')
paddle_b.penup()
paddle_b.goto(350,0)
paddle_b.shapesize(5,1)

ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.dx = 0.15
ball.dy = 0.15

pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.goto(0, 260)
pen.write('Player a: 0 Player b: 0', align='center', font=('courier', 24, 'bold'))
pen.hideturtle()

score_a = 0
score_b = 0

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y += -20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y += -20
    paddle_b.sety(y)



wn.listen()
wn.onkeypress(paddle_a_up, 'w')
wn.onkeypress(paddle_a_down, 's')
wn.onkeypress(paddle_b_up, 'Up')
wn.onkeypress(paddle_b_down, 'Down')




while True:
    wn.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    if ball.ycor() > 290 or ball.ycor() < -290:
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
        ball.dy *= -1

    if ball.xcor() > 390:
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write('Player a: {} player b: {}'.format(score_a, score_b), align='center', font=('courier', 24, 'bold'))
        
    if ball.xcor() < -390:
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write('Player a: {} player b: {}'.format(score_a, score_b), align='center', font=('courier', 24, 'bold'))

    if (ball.xcor() < -340 and ball.xcor() > -350) and \
        (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1 

    if (ball.xcor() > 340 and ball.xcor() < 350) and \
        (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1 