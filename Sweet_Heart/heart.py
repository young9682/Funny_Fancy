import turtle
import math
import random

# ========== 窗口设置 ==========
screen = turtle.Screen()
screen.setup(900, 750)
screen.bgcolor("#0f0f23")
screen.title("❤ SSPU ❤")
screen.tracer(0)          # 关闭自动刷新，手动控制帧

# ========== 背景星空 ==========
stars = turtle.Turtle()
stars.hideturtle()
stars.penup()
stars.speed(0)
for _ in range(150):
    x = random.randint(-440, 440)
    y = random.randint(-360, 360)
    r = random.choice([1, 1, 1, 2, 2, 3])
    stars.goto(x, y)
    stars.dot(r, random.choice(["#ffffff", "#ffd6e8", "#c9b6ff", "#ffe9a8"]))

# ========== 爱心画笔 ==========
heart = turtle.Turtle()
heart.hideturtle()
heart.speed(0)
heart.penup()

# ========== 文字画笔 ==========
txt = turtle.Turtle()
txt.hideturtle()
txt.penup()
txt.color("#ff8fab")


def heart_xy(t, s):
    """爱心参数方程"""
    x = 16 * math.sin(t) ** 3
    y = (13 * math.cos(t) - 5 * math.cos(2 * t)
         - 2 * math.cos(3 * t) - math.cos(4 * t))
    return x * s, y * s + 30


def draw_heart(scale, fill, outline):
    n = 180
    pts = [heart_xy(2 * math.pi * i / n, scale) for i in range(n)]
    heart.clear()
    heart.pencolor(outline)
    heart.fillcolor(fill)
    heart.pensize(2)
    heart.goto(pts[0])
    heart.pendown()
    heart.begin_fill()
    for p in pts[1:]:
        heart.goto(p)
    heart.goto(pts[0])
    heart.end_fill()
    heart.penup()


def beat(x):
    """模拟心跳节律，返回 0~1 的强度"""
    x = x % 1.0
    if x < 0.12:                                  # 第一下（弱）
        return math.sin(x / 0.12 * math.pi) * 0.55
    if x < 0.30:                                  # 第二下（强）
        return math.sin((x - 0.12) / 0.18 * math.pi) * 0.9
    return 0.0


# ========== 固定文字 ==========
txt.goto(0, -250)
txt.write("I ❤ SSPU", align="center", font=("Arial", 34, "bold"))
txt.goto(0, -310)
txt.write("from young86/SSPU-bbt ~ ❤", align="center",
          font=("Microsoft YaHei", 20, "bold"))

screen.update()

# ========== 动画主循环 ==========
frame = 0


def loop():
    global frame
    k = beat(frame / 55.0)                 # 0~1 心跳强度
    scale = 11.0 * (1 + 0.13 * k)          # 呼吸式缩放

    r = 255
    g = int(30 + 110 * k)
    b = int(90 + 110 * k)
    draw_heart(scale, f"#{r:02x}{g:02x}{b:02x}", "#ffb3c1")

    screen.update()
    frame += 1
    screen.ontimer(loop, 25)               # 约 40 帧/秒


loop()
screen.mainloop()