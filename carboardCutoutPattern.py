import turtle

wn = turtle.Screen()
draw = turtle.Turtle()
draw.speed(0)
draw.ht()

def shapeRight(t):
    middle = t.pos()
    print(t.pos())
    t.left(90)
    t.forward(50)
    t.right(90)
    t.forward(5)
    t.left(90)
    t.forward(30)
    t.right(90)
    t.forward(45)
    t.right(122)
    t.forward(95)
    t.right(148)
    return middle

def shapeLeft(t):
    print(t.pos())
    t.forward(51)
    t.left(90)
    t.forward(5)
    t.right(90)
    t.forward(30)
    t.left(90)
    t.forward(45)
    t.left(121.25)
    t.goto(-0.34, -0.56)
    t.right(5.75)


def shape(t):
    shapeRight(t)
    shapeLeft(t)

for i in range(6):
    shape(draw)

wn.exitonclick()
