import math

# Definisikan kelas dasar Shape
class Shape:
    def hitung_luas(self):
        pass

# Definisikan kelas turunan Square yang mewarisi dari Shape
class Square(Shape):
    def __init__(self, sisi):
        self.sisi = sisi

    def hitung_luas(self):
        return self.sisi ** 2

# Definisikan kelas turunan Circle yang mewarisi dari Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    import math

# Definisikan kelas dasar Shape
class Shape:
    def hitung_luas(self):
        pass

# Definisikan kelas turunan Square yang mewarisi dari Shape
class Square(Shape):
    def __init__(self, sisi):
        self.sisi = sisi

    def hitung_luas(self):
        return self.sisi ** 2

# Definisikan kelas turunan Circle yang mewarisi dari Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def hit_luas(self):
        return math.pi * self.radius ** 2

# Definisikan kelas turunan Triangle yang mewarisi dari Shape
class Triangle(Shape):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def hitung_luas(self):
        return 0.5 * self.alas * self.tinggi

# Program utama
if __name__ == "__main__":
    bentuk1 = Square(5)
    bentuk2 = Circle(3)
    bentuk3 = Triangle(4, 6)

    daftar_bentuk = [bentuk1, bentuk2, bentuk3]

    for bentuk in daftar_bentuk:
        luas = bentuk.hitung_luas()
        if isinstance(bentuk, Square):
            print(f"Luas Persegi: {luas}")
        elif isinstance(bentuk, Circle):
            print(f"Luas Lingkaran: {luas}")
        elif isinstance(bentuk, Triangle):
            print(f"Luas Segitiga: {luas}")