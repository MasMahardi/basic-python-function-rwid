
name = [ ]

name.append("Budi")
name.append("Eko")
name.append("Ratna")
name.append("Joko")
name.append("Sultan")
name.append("Vladimir")

print(name)

for i in name:
    print(i)

odd = []
even = []

for i in range(len(name)):
    if i % 2 == 0:
        odd.append(name[i])
    else:
        even.append(name[i])

print(odd)
print(even)

for i in range(len(name)):
    if i % 2 == 0:
        print(f"Halo saya dari tim 1, nama saya {name[i]}")
    else:
        print(f"Halo saya dari tim 2, nama saya {name[i]}")

for i , value in enumerate(name):
    print(f"pendaftar no {i + 1} {value}")

for i in name:
    print(i)
    if i == "Joko":
        break