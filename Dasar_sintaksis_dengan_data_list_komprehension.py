print('\nPerintah del dengan list komprehension')
daftar_buku = ['1.Seven habits', '2.How to influence people', '3.First things first', '4.4Dx']
del daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list komprehension 0:0')
daftar_buku = ['1.Seven habits', '2.How to influence people', '3.First things first', '4.4Dx']
del daftar_buku[0:0]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list komprehension 0:1')
daftar_buku = ['1.Seven habits', '2.How to influence people', '3.First things first', '4.4Dx']
del daftar_buku[0:1]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list komprehension 0:3')
daftar_buku = ['1.Seven habits', '2.How to influence people', '3.First things first', '4.4Dx']
del daftar_buku[0:3]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list komprehension 0:-1')
daftar_buku = ['1.Seven habits', '2.How to influence people', '3.First things first', '4.4Dx']
del daftar_buku[0:-1] #START:END
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list komprehension 0:-2')
daftar_buku = ['1.Seven habits', '2.How to influence people', '3.First things first', '4.4Dx']
del daftar_buku[0:-2] #START:END
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list komprehension 0::2, lompat dari 2 ke 4')
daftar_buku = ['1.Seven habits', '2.How to influence people', '3.First things first', '4.4Dx']
del daftar_buku[0::2] #START:END
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMembuat list baru')
daftar_buku = ['1.Seven habits', '2.How to influence people', '3.First things first', '4.4Dx']
daftar_buku_baru = daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
print('\nMembuat list baru')
del daftar_buku[:]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan komprehension: ganjil')
daftar_buku = ['1.Seven habits', '2.How to influence people', '3.First things first', '4.4Dx']
daftar_buku_baru = daftar_buku[0::2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan komprehension: genap')
daftar_buku = ['1.Seven habits', '2.How to influence people', '3.First things first', '4.4Dx']
daftar_buku_baru = daftar_buku[1::2] #start stop end
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan komprehension: buang diujung')
daftar_buku = ['1.Seven habits', '2.How to influence people', '3.First things first', '4.4Dx']
daftar_buku_baru = daftar_buku[0:-1]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan komprehension: buang diujung dan ke 2')
daftar_buku = ['1.Seven habits', '2.How to influence people', '3.First things first', '4.4Dx']
daftar_buku_baru = daftar_buku[0:-1:2] #start stop end
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan komprehension: ganjil')
daftar_buku = ['1.Seven habits', '2.How to influence people', '3.First things first', '4.4Dx']
print(daftar_buku[0::2])