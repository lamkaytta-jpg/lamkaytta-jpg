import turtle

def gambar_bendera_terbalik():
    screen = turtle.Screen()
    screen.title("Bendera Putih Merah")
    screen.bgcolor("#f0f0f0") 
    
    t = turtle.Turtle()
    t.speed(3)

    def gambar_persegi_panjang(warna, lebar, tinggi):
        t.fillcolor(warna)
        t.begin_fill()
        for _ in range(2):
            t.forward(lebar)
            t.right(90)
            t.forward(tinggi)
            t.right(90)
        t.end_fill()

    t.penup()
    t.goto(-150, 100)
    t.pendown()

    # Putih di atas
    t.pencolor("gray") 
    gambar_persegi_panjang("white", 300, 100)

    t.penup()
    t.goto(-150, 0)
    t.pendown()

    # Merah di bawah
    t.pencolor("black")
    gambar_persegi_panjang("red", 300, 100)

    t.hideturtle()
    screen.mainloop()

# INI BAGIAN YANG TADI SALAH:
if __name__ == "__main__":
    gambar_bendera_terbalik()