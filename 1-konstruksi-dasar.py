# Konstruksi Dasar Python
# Sequential: eksekusi berurutan
print('Hello World')
print('by Imam')
print('Tanggal 12 Februari 2021')
print("-" * 10)

# Percabangan: eksekusi terpilih
ingin_cepat = False
if ingin_cepat:
    print('jalan lurus aja ya!')
else:
    print('jalan lain')

# Perulangan
jumlah_anak = 4

for index_anak in range(1, jumlah_anak + 1):  # jumlah perulangan = 4 - 1 = 3
    print(f'Halo anak #{index_anak}')
