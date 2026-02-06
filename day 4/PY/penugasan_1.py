import tkinter as tk
from tkinter import messagebox

def hitung_total():
    try:
        # Mengambil input dari entry
        harga = float(entry_harga.get())
        kuantitas = float(entry_kuantitas.get())
        
        # Menghitung total
        total = harga * kuantitas
        
        # Menampilkan hasil dengan format dua desimal
        label_hasil.config(text=f"Total: Rp.{total:,.2f}")
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid!")

# Membuat jendela utama
root = tk.Tk()
root.title("Program Kasir")
root.geometry("300x250")
root.configure(padx=20, pady=20)

# Label dan Entry untuk Harga
label_harga = tk.Label(root, text="Harga:")
label_harga.pack(pady=(0, 5))
entry_harga = tk.Entry(root, justify='center')
entry_harga.pack(pady=(0, 10))

# Label dan Entry untuk Kuantitas
label_kuantitas = tk.Label(root, text="Kuantitas:")
label_kuantitas.pack(pady=(0, 5))
entry_kuantitas = tk.Entry(root, justify='center')
entry_kuantitas.pack(pady=(0, 15))

# Tombol Hitung
btn_hitung = tk.Button(root, text="Hitung Total", command=hitung_total)
btn_hitung.pack(pady=(0, 10))

# Label untuk menampilkan Total
label_hasil = tk.Label(root, text="Total: Rp.0.00", font=("Arial", 10, "bold"))
label_hasil.pack()

# Menjalankan aplikasi
root.mainloop()