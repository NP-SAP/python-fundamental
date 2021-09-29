"""
Belajar data list
"""

daftar_buku = ['1.Seven habits', '2.How to influence people', '3.First things first', '4.4Dx']
print(f'daftar buku: {daftar_buku}')

print('\nTampilkan semua isi daftar buku dengan for in')
for buku in daftar_buku:
    print(buku)

print('\nTampilkan isi daftar buku pada indeks tertentu')
print(daftar_buku[0])
print(daftar_buku[2])

print('\nTampilkan dengan for in range')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

daftar_buku = (1, 'Kenji volume 2', -313, 3.14 )
print('\nTampilkan dengan for in range, dimana tipe data tiap elemen berbeda')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nKembalikan nilai awal daftar_buku')
daftar_buku = ['1.Seven habits', '2.How to influence people', '3.First things first', '4.4Dx']
print('\nTambahkan 1 buku baru')
daftar_buku.append('Dunia matematika kelas 5')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nClear list')
daftar_buku.clear()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nGanti elemen pertama')
daftar_buku = ['1.Seven habits', '2.How to influence people', '3.First things first', '4.4Dx']
daftar_buku[0] = '1.Eight Habits'
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nAmbil elemen ke 2')
buku = daftar_buku.pop(1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nTampilkan buku elemen ke 2 yang diambil tadi')
print(buku)

print('\nPop')
daftar_buku = ['1.Seven habits', '2.How to influence people', '3.First things first', '4.4Dx']
daftar_buku.pop()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPop -1')
daftar_buku.pop(-1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del')
daftar_buku = ['1.Seven habits', '2.How to influence people', '3.First things first', '4.4Dx']
del daftar_buku[0]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])



