# Input umur
umur = int(input("Masukkan Umur: "))

# Cek kategori berdasarkan flowchart
if umur <= 10:
    print("Kategori: Anak-anak")
elif umur <= 18:
    print("Kategori: Remaja")
elif umur <= 35:
    print("Kategori: Dewasa")
elif umur <= 65:
    print("Kategori: Parubaya")
else:
    print("Kategori: Tua")

print("Selesai")