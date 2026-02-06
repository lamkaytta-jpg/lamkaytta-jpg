import PySimpleGUI as sg

# Menambahkan teks dan tombol ke dalam layout
layout = [
    [sg.Text("Halo, ini program pertama saya!")],
    [sg.Button("Tutup")]
]

sg.Window(title="Hello World", layout=layout, margins=(100, 50)).read()