"""
Program memghitung luas segitiga
luas segitiga = alas * tinggi /2
"""
print('menghitung luas segitiga')
alas = 10
tinggi = 6
luas_segitiga = alas * tinggi / 2
print(f'Segitiga dengan alas = {alas} dan tinggi = {tinggi} memiliki luas {luas_segitiga}')

print('\nMenghitung luas segitiga 2 dengan copy paste')
alas = 12
tinggi = 8
luas_segitiga = alas * tinggi / 2
print(f'Segitiga dengan alas = {alas} dan tinggi = {tinggi} memiliki luas {luas_segitiga}')

print('\nMembuat fungsi untuk menghitung luas segitiga')
def rumus_luas_segitiga(alas, tinggi) :
    luas_segitiga = alas * tinggi / 2
    return print(f'Luas Segitiga dengan alas = {alas} dan tinggi = {tinggi}, Hasilnya adalah {luas_segitiga}')

rumus_luas_segitiga(10, 6)