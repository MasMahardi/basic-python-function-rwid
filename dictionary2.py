# variable paling sering digunakan pada dictionary
# .keys .items

ID = {
    "Nama" : "Wahyudi",
    "KTP" : 123456,
    "Gol Darah" : "A",
    "Single" : True,
    "Hobbies" : ["Tidur", "Netflix","Coding"],
    "Terdaftar" : False

}
keys = list(ID.keys())
print(keys[2])

ID.setdefault("Address", {"rt" : 10, "rw" : 5, "kecamatan" : "Kejajar", "Kabupate" : "Sleman", "Kota" : "Yogyakarta"})
print(ID)

alamat = ID["Address"]["Kota"]
alamat_2 = ID.get("Address").get("Kota")
print(alamat)
print(alamat_2)