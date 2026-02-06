import turtle

def gambar_bendera():
    # Setup layar
    screen = turtle.Screen()
    screen.title("Bendera Merah Putih - Indonesia")
    
    t = turtle.Turtle()
    t.speed(3) # Kecepatan menggambar

    # Fungsi untuk membuat persegi panjang
    def gambar_persegi_panjang(warna, lebar, tinggi):
        t.fillcolor(warna)
        t.begin_fill()
        for _ in range(2):
            t.forward(lebar)
            t.right(90)
            t.forward(tinggi)
            t.right(90)
        t.end_fill()

    # Pindah ke posisi awal (agar bendera di tengah)
    t.penup()
    t.goto(-150, 100)
    t.pendown()

    # Bagian Merah
    gambar_persegi_panjang("red", 300, 100)

    # Pindah posisi ke bagian bawah untuk warna putih
    t.penup()
    t.goto(-150, 0)
    t.pendown()

    # Bagian Putih
    gambar_persegi_panjang("white", 300, 100)

    # Sembunyikan kura-kura dan tampilkan hasil
    t.hideturtle()
    screen.mainloop()

# Memanggil fungsi
if __name__ == "__main__":
    gambar_bendera()