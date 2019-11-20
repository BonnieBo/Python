import  turtle
turtle.title('正方体')
n = 100  # 边长

# 正面
turtle.begin_fill()
turtle.fillcolor('#069')
for x in range(4):
    turtle.forward(n)
    turtle.right(90)
turtle.end_fill()
# 上面
turtle.begin_fill()
turtle.fillcolor('#ccc')
turtle.left(45)
turtle.forward(n * 0.6)
turtle.right(45)
turtle.forward(n)
turtle.right(135)
turtle.forward(n * 0.6)
turtle.end_fill()
# 右侧
turtle.up()
turtle.goto(n, -n)
turtle.down()
turtle.left(180)
turtle.forward(n*0.6)
turtle.left(45)
turtle.forward(n)

turtle.hideturtle()
turtle.done()
