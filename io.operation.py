text = "Hello World"
#kata kunci with dan fungsi open

with open("output.txt", "w") as file:
    file.write(text)

with open("output.txt", "r") as file:
    data = file.read()
print(data)