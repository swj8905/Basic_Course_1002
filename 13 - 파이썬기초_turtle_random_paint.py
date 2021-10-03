import turtle as t
import random

t.shape("turtle")
t.speed(100)
color = ["red", "blue", "green", "yellow", "purple", "orange"]
function_list = [t.forward, t.backward, t.left, t.right, t.dot, t.circle]
while True:
    r = random.randint(0,50)
    t.color(random.choice(color))
    random.choice(function_list)(r)

t.done()