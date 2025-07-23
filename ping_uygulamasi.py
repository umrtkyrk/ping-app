import tkinter as tk
from tkinter import messagebox, scrolledtext
import subprocess
import threading

def ping_at():
    hedef = entry.get()
    sayi = count_entry.get()

    if not hedef:
        messagebox.showwarning("Uyarı", "Lütfen bir adres girin.")
        return

    if not sayi.isdigit():
        messagebox.showwarning("Uyarı", "Lütfen geçerli bir sayı girin.")
        return

    output.delete("1.0", tk.END)
    output.insert(tk.END, "Ping işlemi başlatılıyor...\n")
    buton.config(state="disabled")
    threading.Thread(target=ping_islemi, args=(hedef, int(sayi))).start()

def ping_islemi(hedef, sayi):
    try:
        sonuc = subprocess.run(["ping", "-c", str(sayi), hedef], capture_output=True, text=True)
        output.insert(tk.END, sonuc.stdout)
        if "0 packets received" in sonuc.stdout:
            messagebox.showerror("Sonuç", "Ping başarısız. Sunucuya ulaşılamadı.")
        else:
            messagebox.showinfo("Sonuç", "Ping başarılı!")
    except Exception as e:
        messagebox.showerror("Hata", f"Bir hata oluştu: {e}")
    finally:
        buton.config(state="normal")

def temizle():
    output.delete("1.0", tk.END)
    entry.delete(0, tk.END)
    count_entry.delete(0, tk.END)

# Arayüz Oluşturma
pencere = tk.Tk()
pencere.title("Ping Test Uygulaması (macOS GUI)")
pencere.geometry("550x500")

# Ping adresi
etiket = tk.Label(pencere, text="Ping Atılacak Adresi Girin:")
etiket.pack(pady=5)
entry = tk.Entry(pencere, width=50)
entry.pack(pady=5)

# Ping sayısı
count_label = tk.Label(pencere, text="Kaç kez ping atılsın?")
count_label.pack()
count_entry = tk.Entry(pencere, width=10)
count_entry.pack(pady=5)

# Butonlar
buton = tk.Button(pencere, text="Ping At", command=ping_at)
buton.pack(pady=10)

clear_button = tk.Button(pencere, text="Temizle", command=temizle)
clear_button.pack()

# Çıktı kutusu
output = scrolledtext.ScrolledText(pencere, height=20, width=65)
output.pack(pady=10)

pencere.mainloop()
