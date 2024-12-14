import time
import tkinter as tk
from tkinter import messagebox

# Puanların tutulduğu liste
puan_listesi = []

# Performans Hesaplama Fonksiyonu
def performans_hesapla():
    try:
        # Giriş verilerini al
        takim = entry_takim.get().strip()
        otonom_kale = entry_otonom_kale.get().strip()
        otonom_yan = entry_otonom_yan.get().strip()
        teleop_kale = entry_teleop_kale.get().strip()
        teleop_yan = entry_teleop_yan.get().strip()
        feed = entry_feed.get().strip().lower()
        asilma = entry_asilma.get().strip().lower()

        # Eksik veri kontrolü
        if not (takim and otonom_kale and otonom_yan and teleop_kale and teleop_yan and feed and asilma):
            messagebox.showerror("Hata", "Lütfen tüm alanları eksiksiz doldurun.")
            return

        # Sayısal giriş doğrulaması
        takim = int(takim)
        otonom_kale = int(otonom_kale)
        otonom_yan = int(otonom_yan)
        teleop_kale = int(teleop_kale)
        teleop_yan = int(teleop_yan)

        if feed not in ["evet", "hayır"] or asilma not in ["evet", "hayır"]:
            messagebox.showerror("Hata", "Feed ve Asılma alanları 'Evet' veya 'Hayır' olmalıdır.")
            return

        # Performans Kontrolleri
        print("İstatistikler Hesaplanıyor...")
        time.sleep(2)

        toplam_puan = otonom_kale + otonom_yan + teleop_kale + teleop_yan
        puan = toplam_puan / 3

        if (otonom_kale >= 5 and otonom_yan >= 2 and teleop_kale >= 20 and teleop_yan >= 10):
            sonuc = f"{takim} numaralı takım bu raunt iyi bir performans sergiledi!"
        elif (otonom_kale == 5 and otonom_yan == 2 and teleop_kale == 20 and teleop_yan == 10):
            sonuc = f"{takim} numaralı takım bu raunt ortalama bir performans sergiledi!"
        else:
            sonuc = f"{takim} numaralı takım bu raunt kötü bir performans sergiledi!"

        # Puanları listeye ekle
        puan_listesi.append((takim, puan))

        messagebox.showinfo("Sonuç", sonuc)
        messagebox.showinfo("Puan", f"Puan: {puan:.2f}")

    except ValueError:
        messagebox.showerror("Hata", "Sayısal alanlara yalnızca rakam girin.")

# Puanları Sıralama ve Gösterme Fonksiyonu
def puanlari_goster():
    if not puan_listesi:
        messagebox.showerror("Hata", "Henüz hiçbir takımın puanı kaydedilmedi.")
        return

    # Yeni bir pencere oluştur
    puan_penceresi = tk.Toplevel(root)
    puan_penceresi.title("Takım Puanları")

    # Puanları sıralama
    sorted_puanlar = sorted(puan_listesi, key=lambda x: x[1], reverse=True)

    # Sıralamayı göster
    tk.Label(puan_penceresi, text="Takım Numarası", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=10, pady=5)
    tk.Label(puan_penceresi, text="Puan", font=("Arial", 12, "bold")).grid(row=0, column=1, padx=10, pady=5)

    for idx, (takim, puan) in enumerate(sorted_puanlar, start=1):
        tk.Label(puan_penceresi, text=f"{takim}", font=("Arial", 10)).grid(row=idx, column=0, padx=10, pady=5)
        tk.Label(puan_penceresi, text=f"{puan:.2f}", font=("Arial", 10)).grid(row=idx, column=1, padx=10, pady=5)

# Arayüz Başlatma
root = tk.Tk()
root.title("FRC Analitik Gözlemleme Arayüzü")

# Giriş Alanları
tk.Label(root, text="Takım Numarası:").grid(row=0, column=0, padx=5, pady=5)
entry_takim = tk.Entry(root)
entry_takim.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Otonom KALE Atışı:").grid(row=1, column=0, padx=5, pady=5)
entry_otonom_kale = tk.Entry(root)
entry_otonom_kale.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Otonom YAN KALE Atışı:").grid(row=2, column=0, padx=5, pady=5)
entry_otonom_yan = tk.Entry(root)
entry_otonom_yan.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="Teleop KALE Atışı:").grid(row=3, column=0, padx=5, pady=5)
entry_teleop_kale = tk.Entry(root)
entry_teleop_kale.grid(row=3, column=1, padx=5, pady=5)

tk.Label(root, text="Teleop YAN KALE Atışı:").grid(row=4, column=0, padx=5, pady=5)
entry_teleop_yan = tk.Entry(root)
entry_teleop_yan.grid(row=4, column=1, padx=5, pady=5)

tk.Label(root, text="Feed Yapıldı mı? (Evet/Hayır):").grid(row=5, column=0, padx=5, pady=5)
entry_feed = tk.Entry(root)
entry_feed.grid(row=5, column=1, padx=5, pady=5)

tk.Label(root, text="Robot Asıldı mı? (Evet/Hayır):").grid(row=6, column=0, padx=5, pady=5)
entry_asilma = tk.Entry(root)
entry_asilma.grid(row=6, column=1, padx=5, pady=5)

# Hesaplama Butonu
hesapla_butonu = tk.Button(root, text="Performansı Hesapla", command=performans_hesapla)
hesapla_butonu.grid(row=7, column=0, pady=10)

# Puanları Göster Butonu
puanlari_goster_butonu = tk.Button(root, text="Puanları Göster", command=puanlari_goster)
puanlari_goster_butonu.grid(row=7, column=1, pady=10)

# Uygulama Başlatma
root.mainloop()
