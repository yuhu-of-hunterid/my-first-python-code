'''
program perulangan membaca buku dengan while
'''
jumlah_buku = 10
print('ibu berkata, "baca semua bukumu"')
total_jumlah_baca = 0

jumlah_paham = 0
print(f'jumlah buku yang sudah dibaca dan di pahami {jumlah_paham}')

while total_jumlah_baca < jumlah_buku * 2:
    total_jumlah_baca = total_jumlah_baca + 1
    if jumlah_paham == 9:
        print(f"buku ke {jumlah_paham} belum paham")
    else:
        jumlah_paham = jumlah_paham + 1
        print(f"Buku ke {jumlah_paham} sudah dibaca dan dipahami")

print(f'jumlah buku yang sudah dibaca {jumlah_paham}')
if jumlah_paham == jumlah_buku:
    print('"Bu,semua buku sudah dibaca dan dipahami')
else:
    print(f'"Bu, tidak semua buku bisa dipahami. '
          f'Budi hanya bisa memahami {jumlah_paham} buku')
