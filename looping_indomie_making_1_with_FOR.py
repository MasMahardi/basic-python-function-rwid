"""
Semua Sintaksis tentang
1. Sekuensial
2. Percabangan
3. Perulangan
"""

#Branching

cabe = 100
cabe_yang_dimasukkan = 0


print("Buat Indomie")
print("Panaskan Air")
print("Masukkan Mie")
print("Masak Air hingga mendidih")
print("Lettakn Mie di piring")
print("Campurkan Bumbu")

for cabe_yang_dimasukkan in range(1,cabe + 1):
    print(f"Masukkan Cabe ke {cabe_yang_dimasukkan} ke dalam piring berisikan Indomie")

print(f"Indomienya pake {cabe_yang_dimasukkan} cabe nieh, ASEKK!!")