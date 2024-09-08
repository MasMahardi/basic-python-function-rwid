"""
Semua Sintaksis tentang
1. Sekuensial
2. Percabangan
3. Perulangan
"""

#Branching

saus_sambal = 3
cabe = 1
Merica = 1


print("Buat Indomie")
print("Panaskan Air")
print("Masukkan Mie")
print("Masak Air hingga mendidih")
print("Lettakn Mie di piring")
print("Campurkan Bumbu")

if 1 <= saus_sambal <=3:
    print(f"Masukkan Saus Sambal {saus_sambal}")
    print("Indomie pedas siap disajikan")
elif saus_sambal >=4:
    print(f"Masukkan Saus Sambal {saus_sambal}")
    print("Indomie nya Pedes banget nih, siapa sih yang bikin!!!")
else:
    print("Terpaksa G Pake Sambel")
    print("Indomienya Ga Pedes Nieh, yah mo gimana lagi daripada ga makan!")