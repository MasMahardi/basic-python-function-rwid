"""
Semua Sintaksis tentang
1. Sekuensial
2. Percabangan
3. Perulangan
"""

#Branching

saus_sambal = 5
cabe = 0
Merica = 0


print("Buat Indomie")
print("Panaskan Air")
print("Masukkan Mie")
print("Masak Air hingga mendidih")
print("Lettakn Mie di piring")
print("Campurkan Bumbu")

if 1 <= saus_sambal <=3:
    print(f"Masukkan Saus Sambal {saus_sambal}")
    print("Indomie pedas siap disajikan")
elif saus_sambal >3:
    print(f"Masukkan Saus Sambal {saus_sambal}")
    print("GILEEE INDOMIE nya PEDES BEUD!!!!!")
elif saus_sambal ==0 and cabe > 0:
    print(f"Masukkan Cabe {cabe}")
    print("Indomie nya Pedes Cabe siap disajikan")
elif cabe ==0 and saus_sambal==0 and Merica > 0:
    print(f"Masukkan Merica {Merica}")
    print("Indomie nya Pedes Merica siap disajikan")
else:
    print("Terpaksa G Pake Sambel")
    print("Indomienya Ga Pedes Nieh, yah mo gimana lagi daripada ga makan!")