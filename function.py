# function, sebuat metode untuk menulis kode tertentu dengan harapan kode tersebut bisa iulang2/ diiterasi
# untuk membuat function, menggunakan kata kunci def()
from Tools.scripts.generate_global_objects import Printer


def sum(x):
    output = x + 10
    return  output

hasil = sum (10)
print(hasil)

def introduction(name, age):
    output = f"My name is {name}, I'm {age} years old"
    return output

tes = introduction("HARDJO", 35)
print(tes)

