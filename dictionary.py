# dictionary tipe data yang memiliki tipe hubungan key : value
## biasanya berformat JSON atau GeoJSON

ID = {
    "Nama" : "Wahyudi",
    "KTP" : 123456,
    "Gol Darah" : "A",
    "Single" : True,
    "Hobbies" : ["Tidur", "Netflix","Coding"],
    "Terdaftar" : False

}

print(ID)
print("------------------------------------------------------")

hobi = ID["Hobbies"][2]
print(hobi)

print("------------------------------------------------------")

# .get() dalam method . get jika key yang dipassing tidak ada makan akan mengeluarkan nilai Nan
hobi_ke_2 = ID.get("Hobbies", "Terdaftar")
print(hobi_ke_2)

print("------------------------------------------------------")
#.setdefault( -> menambahkan key value baru dalam dictionary jika key yang diberikan ngga ada di dalam dictionary
ID_2 = {
    "Nama" : "Wahyudi",
    "KTP" : 123456,
    "Gol Darah" : "A",
    "Single" : True,
    "Hobbies" : ["Tidur", "Netflix","Coding"],
    "Terdaftar" : False

}
ID_2.setdefault("Alamat:", "Jalan Nangka No.77")
print(ID_2)