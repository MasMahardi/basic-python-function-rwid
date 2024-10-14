queue = [ ]

queue.append("Budi")
queue.append("Joko")
queue.append("Wati")
queue.append("Rudi")
queue.append("Akmal")

print(queue)

# Jika menggunakan for maka bisa dilakukan looping
for i in range(3):
    queue.pop(0)

print(queue)

# Jika menggunakan 0 maka yang terindeks dan dihapus adalah yg awal
queue.pop(0)
print(queue)

# Jika tanpa 0 maka yang terindeks dan dihapus adalah yg akhir (Menjadi Array)
queue.pop()
print(queue)

# Jika tanpa 0 maka yang terindeks dan dihapus adalah yg akhir (Menjadi Array)
