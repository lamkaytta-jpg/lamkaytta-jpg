import tkinter as tk
from tkinter import ttk, messagebox

def hitung_dan_simpan():
    try:
        nopol = entry_nopol.get()
        masuk = int(entry_masuk.get())
        keluar = int(entry_keluar.get())
        
        if keluar < masuk:
            messagebox.showwarning("Input Salah", "Waktu keluar tidak boleh lebih kecil dari masuk!")
            return

        durasi = keluar - masuk
        biaya = durasi * 2000
        
        # Update field biaya
        entry_biaya.config(state='normal')
        entry_biaya.delete(0, tk.END)
        entry_biaya.insert(0, str(biaya))
        entry_biaya.config(state='readonly')

        # Masukkan ke tabel (simulasi urut terakhir keluar)
        tree_terakhir.insert('', 0, values=(nopol, masuk, keluar, f"Rp {biaya}"))
        # Masukkan ke tabel (simulasi list banyak bayar)
        tree_banyak.insert('', tk.END, values=(nopol, masuk, keluar, f"Rp {biaya}"))
        
    except ValueError:
        messagebox.showerror("Error", "Masukkan jam dalam format angka (contoh: 8, 10)")

def cari_nopol():
    target = entry_cari.get()
    messagebox.showinfo("Cari", f"Mencari NoPol: {target}...")

root = tk.Tk()
root.title("Aplikasi Parkir Kelompok 6")
root.geometry("800x500")

# --- Bagian Atas: Input ---
header = tk.Label(root, text="Aplikasi Parkir Kelompok 6", font=("Arial", 16, "bold"))
header.grid(row=0, column=0, columnspan=3, pady=10, padx=10, sticky="w")

# Kiri: Form Input
frame_input = tk.Frame(root)
frame_input.grid(row=1, column=0, padx=20, sticky="n")

labels = ["Cari NoPol", "No Plat Polisi", "Waktu Masuk", "Waktu Keluar", "Biaya"]
entries = []

for i, text in enumerate(labels):
    tk.Label(frame_input, text=text).grid(row=i, column=0, sticky="w", pady=5)
    
entry = tk.Entry(frame_input, width=25)
entry.grid(row=0, column=1, padx=5)
entry_cari = entry # Khusus untuk cari

btn_cari = tk.Button(frame_input, text="Cari", command=cari_nopol)
btn_cari.grid(row=0, column=2)

entry_nopol = tk.Entry(frame_input, width=30)
entry_nopol.grid(row=1, column=1, columnspan=2)

entry_masuk = tk.Entry(frame_input, width=30)
entry_masuk.grid(row=2, column=1, columnspan=2)

entry_keluar = tk.Entry(frame_input, width=30)
entry_keluar.grid(row=3, column=1, columnspan=2)

entry_biaya = tk.Entry(frame_input, width=20)
entry_biaya.insert(0, "0")
entry_biaya.config(state='readonly')
entry_biaya.grid(row=4, column=1, sticky="w")

btn_hitung = tk.Button(frame_input, text="Button", command=hitung_dan_simpan)
btn_hitung.grid(row=4, column=2)

# Kanan: Banner Harga
frame_harga = tk.Frame(root)
frame_harga.grid(row=1, column=1, columnspan=2, padx=50)

tk.Label(frame_harga, text="Biaya Per Jam", font=("Comic Sans MS", 18, "bold"), fg="red").pack()
tk.Label(frame_harga, text="Rp. 2.000", font=("Arial", 40, "bold"), fg="red").pack()

# --- Bagian Bawah: Tabel ---
columns = ("No Plat Polisi", "Masuk", "Keluar", "Biaya")

# Tabel 1
tk.Label(root, text="List Pelanggan Urut Terakhir Keluar", fg="blue").grid(row=2, column=0, pady=(20,0))
tree_terakhir = ttk.Treeview(root, columns=columns, show='headings', height=6)
for col in columns:
    tree_terakhir.heading(col, text=col)
    tree_terakhir.column(col, width=80)
tree_terakhir.grid(row=3, column=0, padx=10, pady=5)

# Tabel 2
tk.Label(root, text="List Pelanggan Banyak Bayar", fg="blue").grid(row=2, column=1, pady=(20,0))
tree_banyak = ttk.Treeview(root, columns=columns, show='headings', height=6)
for col in columns:
    tree_banyak.heading(col, text=col)
    tree_banyak.column(col, width=80)
tree_banyak.grid(row=3, column=1, padx=10, pady=5)

root.mainloop()