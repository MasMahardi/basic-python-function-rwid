"""
Semua Sintaksis tentang
1. Sekuensial
2. Percabangan
3. Perulangan
"""

#Branching

cabe = 10
cabe_yang_dimasukkan_tidak_busuk = 0


print("Buat Indomie")
print("Panaskan Air")
print("Masukkan Mie")
print("Masak Air hingga mendidih")
print("Lettakn Mie di piring")
print("Campurkan Bumbu")

while cabe_yang_dimasukkan_tidak_busuk < cabe:
    cabe_yang_dimasukkan_tidak_busuk = cabe_yang_dimasukkan_tidak_busuk + 1
    if cabe_yang_dimasukkan_tidak_busuk == 10:
        print(f" Cabe ke {cabe_yang_dimasukkan_tidak_busuk } adalah busuk")
    else:
        print(f" Cabe ke {cabe_yang_dimasukkan_tidak_busuk} tidak busuk")

