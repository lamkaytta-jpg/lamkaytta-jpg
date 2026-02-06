import turtle
import math

# Setup Layar
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("#050505") # Hitam pekat luar angkasa
screen.tracer(0) # Menghilangkan jeda gambar agar langsung muncul

t = turtle.Turtle()
t.hideturtle()

def draw_ellipse(x, y, radius_x, radius_y, color, thickness):
    t.penup()
    t.goto(x + radius_x, y)
    t.pendown()
    t.color(color)
    t.pensize(thickness)
    
    # Menggambar elips dengan kalkulasi matematika (sin/cos)
    for i in range(361):
        angle = math.radians(i)
        tx = x + radius_x * math.cos(angle)
        ty = y + radius_y * math.sin(angle)
        t.goto(tx, ty)

def draw_saturn_pro():
    # 1. Gambar Bintang Acak di Latar Belakang
    import random
    star = turtle.Turtle()
    star.hideturtle()
    star.speed(0)
    star.color("white")
    for _ in range(50):
        star.penup()
        star.goto(random.randint(-400, 400), random.randint(-300, 300))
        star.dot(random.randint(1, 3))

    # 2. Gambar Cincin Bagian Belakang (Hanya setengah atas)
    # Kita gambar beberapa lapis untuk efek gradien cincin
    ring_colors = ["#4d4433", "#8c7e62", "#5e5441"]
    for i, col in enumerate(ring_colors):
        draw_ellipse(0, 0, 220 - (i*5), 60 - (i*2), col, 2)

    # 3. Gambar Planet dengan Efek Shadow (Gradien Sederhana)
    # Menggambar lingkaran bertumpuk dari gelap ke terang
    planet_colors = ["#635532", "#8c7741", "#bda25c", "#e3c16f", "#f5e2ab"]
    for i, col in enumerate(planet_colors):
        t.penup()
        # Geser sedikit setiap lapis untuk efek cahaya dari samping
        t.goto(0 - (i*5), -100 + (i*2)) 
        t.pendown()
        t.color(col)
        t.begin_fill()
        t.circle(100 - (i*3))
        t.end_fill()

    # 4. Gambar Cincin Bagian Depan (Hanya setengah bawah)
    # Trik: Kita gambar ulang elips tapi hanya setengah putaran agar menutupi planet
    t.penup()
    t.pensize(3)
    for i, col in enumerate(ring_colors):
        radius_x = 220 - (i*5)
        radius_y = 60 - (i*2)
        t.color(col)
        # Mulai dari sudut 180 derajat ke 360 (setengah bawah)
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

    screen.update() # Tampilkan semua gambar sekaligus

draw_saturn_pro()
screen.mainloop()