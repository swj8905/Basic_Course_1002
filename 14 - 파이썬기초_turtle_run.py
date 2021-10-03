# 터틀런
import turtle as t
import random

joker = t.Turtle()     # 악당 거북이를 생성
joker.shape("turtle")
joker.color("red")
joker.speed(0)
joker.up()
joker.goto(0, 200)   # 악당 거북이 초기 위치 설정

food = t.Turtle()    # 먹이 생성
food.shape("circle")
food.color("green")
food.speed(0)
food.up()
food.goto(0, -200)  # 먹이 초기 위치 설정

def turn_right():  # 오른쪽으로 방향을 바꿉니다.
    t.setheading(0)


def turn_up():  # 위로 방향을 바꿉니다.
    t.setheading(90)


def turn_left():  # 왼쪽으로 방향을 바꿉니다.
    t.setheading(180)


def turn_down():  # 아래로 방향을 바꿉니다.
    t.setheading(270)


def play():
    t.forward(10)
    ang = joker.towards(t.pos())
    joker.setheading(ang)
    joker.forward(9)
    if t.distance(food) < 12:
        star_x = random.randint(-230, 230)
        star_y = random.randint(-230, 230)
        food.goto(star_x, star_y)
    if t.distance(joker) >= 12:
        t.ontimer(play, 100)


t.setup(500, 500)
t.bgcolor("orange")
t.shape("turtle")
t.speed(0)
t.up()
t.color("white")
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.listen()
play()
t.mainloop()