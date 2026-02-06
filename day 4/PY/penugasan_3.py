import tkinter as tk
from tkinter import messagebox

def simpan_data():
    nama = entry_nama.get()
    if nama:
        messagebox.showinfo("Sukses", f"Data {nama} berhasil disimpan!")
    else:
        messagebox.showwarning("Peringatan", "Nama Lengkap harus diisi!")

def hapus_form():
    for entry in list_entries:
        entry.delete(0, tk.END)
    txt_alamat.delete("1.0", tk.END)

root = tk.Tk()
root.title("Formulir Siswa Baru")
root.geometry("600x700")
root.configure(bg="#cccccc")

# Header Biru
header_frame = tk.Frame(root, bg="#a0e4f1", height=50)
header_frame.pack(fill="x")
tk.Label(header_frame, text="DATA SISWA BARU", font=("Arial", 14, "bold"), bg="#a0e4f1").pack(pady=10)

# Container Form
form_frame = tk.Frame(root, bg="#cccccc", padx=40, pady=20)
form_frame.pack(fill="both", expand=True)

labels = ["Nama Lengkap", "Tanggal Lahir", "Asal Sekolah", "NISN", "Nama Ayah", "Nama Ibu", "Nomor Telepon / HP"]
list_entries = []

for label_text in labels:
    tk.Label(form_frame, text=label_text, bg="#cccccc", anchor="w").pack(fill="x")
    e = tk.Entry(form_frame, font=("Arial", 11))
    e.pack(fill="x", pady=(0, 10))
    list_entries.append(e)

# Khusus Alamat (Text Box Besar)
tk.Label(form_frame, text="Alamat", bg="#cccccc", anchor="w").pack(fill="x")
txt_alamat = tk.Text(form_frame, height=5, font=("Arial", 11))
txt_alamat.pack(fill="x", pady=(0, 20))

# Tombol di bawah
btn_frame = tk.Frame(root, bg="#5da7a7", pady=10)
btn_frame.pack(fill="x", side="bottom")

entry_nama = list_entries[0] # Referensi untuk fungsi simpan

tk.Button(btn_frame, text="Simpan", bg="#c06040", fg="white", width=12, command=simpan_data).pack(side="right", padx=20)
tk.Button(btn_frame, text="Hapus", bg="#c06040", fg="white", width=12, command=hapus_form).pack(side="right")

root.mainloop()