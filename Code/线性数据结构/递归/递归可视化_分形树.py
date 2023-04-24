import turtle
t = turtle.Turtle()

# def drawSpiral(t, lineLen):
#     if lineLen > 0:
#         t.forward(lineLen)
#         t.right(90)
#         drawSpiral(t, lineLen-5)

# drawSpiral(t, 100)
def tree(branchLen, t):
    if branchLen > 5: # 最小问题
        t.forward(branchLen) # 画树枝
        t.right(20) # 右转20度
        tree(branchLen-15, t) # 递归调用
        t.left(40) # 左转40度
        tree(branchLen-15, t) # 递归调用
        t.right(20) # 右转20度. 回到原来的方向
        t.backward(branchLen) # 回到原来的位置

t.left(90) # 左转90度
t.up() # 抬起画笔
t.backward(100) # 后退100
t.down() # 放下画笔
t.color("green") # 设置画笔颜色
t.pensize(3) # 设置画笔粗细
tree(75, t) # 递归调用
t.hideturtle() # 隐藏画笔

turtle.done()