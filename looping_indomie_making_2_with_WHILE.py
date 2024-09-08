"""
Semua Sintaksis tentang
1. Sekuensial
2. Percabangan
3. Perulangan
"""

#Branching

cabe = 10
cabe_yang_dimasukkan = 0


print("Buat Indomie")
print("Panaskan Air")
print("Masukkan Mie")
print("Masak Air hingga mendidih")
print("Lettakn Mie di piring")
print("Campurkan Bumbu")

while cabe_yang_dimasukkan < cabe:
    cabe_yang_dimasukkan = cabe_yang_dimasukkan + 1
    print(f"Masukkan cabe ke {cabe_yang_dimasukkan} ke piring berisi indomie")

print(f"Indomienya pake {cabe_yang_dimasukkan} cabe nieh, ASEKK!!")