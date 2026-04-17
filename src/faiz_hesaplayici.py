import tkinter as tk
from tkinter import messagebox

def faiz_hesapla():
    try:
        anapara = float(entry_anapara.get())
        oran = float(entry_oran.get())
        vade = float(entry_vade.get())
        faiz = anapara * oran * vade / 100
        toplam = anapara + faiz
        label_sonuc.config(text=f"Faiz: {faiz:.2f} TL\nToplam: {toplam:.2f} TL")
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli sayı girin.")

root = tk.Tk()
root.title("Basit Faiz Hesaplayıcı")

label_anapara = tk.Label(root, text="Ana Para (TL):")
label_anapara.pack()
entry_anapara = tk.Entry(root)
entry_anapara.pack()

label_oran = tk.Label(root, text="Faiz Oranı (%):")
label_oran.pack()
entry_oran = tk.Entry(root)
entry_oran.pack()

label_vade = tk.Label(root, text="Vade (Yıl):")
label_vade.pack()
entry_vade = tk.Entry(root)
entry_vade.pack()

btn_hesapla = tk.Button(root, text="Hesapla", command=faiz_hesapla)
btn_hesapla.pack(pady=10)

label_sonuc = tk.Label(root, text="")
label_sonuc.pack()

root.mainloop()
