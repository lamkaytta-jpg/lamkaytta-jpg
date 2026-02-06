# 1. Input Nama dan Gaji Pokok
nama = input("Masukkan Nama Karyawan: ")
gaji_pokok = float(input("Masukkan Gaji Pokok: "))

# 2. Proses Perhitungan
# Tunjangan = 20% x Gaji_Pokok
tunjangan = 0.20 * gaji_pokok

# Pajak = 15% x (Gaji_Pokok + Tunjangan)
pajak = 0.15 * (gaji_pokok + tunjangan)

# Gaji_Bersih = Gaji_Pokok + Tunjangan - Pajak
gaji_bersih = gaji_pokok + tunjangan - pajak

# 3. Output Nama, Gaji Pokok, dan Gaji Bersih
print("\n--- Slip Gaji Karyawan ---")
print(f"Nama         : {nama}")
print(f"Gaji Pokok   : Rp{gaji_pokok:,.2f}")
print(f"Gaji Bersih  : Rp{gaji_bersih:,.2f}")