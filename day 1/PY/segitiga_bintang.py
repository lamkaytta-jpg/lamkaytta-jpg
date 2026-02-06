print("Segitiga Bintang Siku Siku")
baris = int(input("Masukkan jumlah baris: "))

for i in range(1, baris + 1):
    for j in range(i):
        print("* ", end="")
    print()
