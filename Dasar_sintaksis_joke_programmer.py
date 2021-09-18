"""
Semua sintaksis dasar bahasa pemrograman terdiri dari:
1. Sekuensial: langkah berurutan
2. Percabangan: langkah melompat jika kondisi terpenuhi
3. Perulangan: langkah mengulang yang sama berkali-kali sampai/selama kondisi terpenuhi
"""

# Sekuensial
print('Ibu berkata, "pergi ke toko"')
print('Budi menjawab,"baik, apa yang harus saya lakukan di toko?"')
print('Ibu menjawab, "beli satu botol susu, dan jika ada telur beli 6 butir telur"')
print('Maka Budi berangkat ke toko dan mulai berbelanja"')

# Percabangan
jumlah_botol_susu = 150
jumlah_butir_telur = 1000
print(f"jumlah botol susu {jumlah_botol_susu} botol")
print(f"jumlah butir telur {jumlah_butir_telur} butir")

if jumlah_botol_susu > 0:
    print("Budi mengecek harganya, dan ternyata uangnya cukup")
    if jumlah_butir_telur > 0:
        print("Budi membeli 1 botol susu dan 6 butir telur")
    else:
        print("Budi membeli 1 botol susu")

else:
    print("Budi tidak jadi membeli 1 botol susu")

print("Budi pulang ke rumah")
print("Menyampaikan hasilnya kepada ibu")


