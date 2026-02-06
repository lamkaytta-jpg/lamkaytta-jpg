import turtle
import math
import random

# Setup Layar
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("#02040a") # Hitam kebiruan sangat gelap
screen.tracer(0) 

t = turtle.Turtle()
t.hideturtle()

def draw_ellipse(x, y, radius_x, radius_y, color, thickness):
    t.penup()
    t.goto(x + radius_x, y)
    t.pendown()
    t.color(color)
    t.pensize(thickness)
    for i in range(361):
        angle = math.radians(i)
        tx = x + radius_x * math.cos(angle)
        ty = y + radius_y * math.sin(angle)
        t.goto(tx, ty)

def draw_blue_saturn():
    # 1. Bintang-bintang
    star = turtle.Turtle()
    star.hideturtle()
    star.color("white")
    for _ in range(60):
        star.penup()
        star.goto(random.randint(-400, 400), random.randint(-300, 300))
        star.dot(random.randint(1, 3))

    # 2. Cincin Bagian Belakang (Warna Biru Abu-abu)
    ring_colors = ["#1b263b", "#415a77", "#778da9"]
    for i, col in enumerate(ring_colors):
        draw_ellipse(0, 0, 230 - (i*8), 65 - (i*3), col, 2)

    # 3. Planet Biru dengan Efek Shading
    # Dari biru gelap (bayangan) ke biru muda terang (cahaya)
    planet_colors = ["#0d1b2a", "#1b263b", "#415a77", "#778da9", "#e0e1dd"]
    for i, col in enumerate(planet_colors):
        t.penup()
        t.goto(0 - (i*6), -100 + (i*2.5)) 
        t.pendown()
        t.color(col)
        t.begin_fill()
        t.circle(100 - (i*4))
        t.end_fill()

    # 4. Cincin Bagian Depan (Efek Transparan Sederhana)
    for i, col in enumerate(ring_colors):
        radius_x = 230 - (i*8)
        radius_y = 65 - (i*3)
        t.color(col)
        t.pensize(3)
        for angle_deg in range(180, 361):
            angle = math.radians(angle_deg)
            tx = 0 + radius_x * math.cos(angle)
            ty = 0 + radius_y * math.sin(angle)
            if angle_deg == 180:
                t.penup()
                t.goto(tx, ty)
                t.pendown()
            else:
                t.goto(tx, ty)

    screen.update()

draw_blue_saturn()
screen.mainloop()