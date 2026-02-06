while True:
    # 1. Input nilai siswa
    nilai_siswa = float(input("Masukkan nilai siswa: "))

    # 2. Cek apakah nilai >= 75
    if nilai_siswa >= 75:
        print("Tuntas")
        break  # Alur berakhir (End)
    else:
        # 3. Jika tidak, tanya apakah ingin mengulang
        mengulang = input("Apakah ingin mengulang? (Ya/Tidak): ")
        
        # 4. Cek input mengulang
        if mengulang.capitalize() != "Ya":
            print("Tidak Tuntas")
            break  # Alur berakhir (End)
        
        # Jika mengulang = "Ya", loop akan berlanjut kembali ke input nilai