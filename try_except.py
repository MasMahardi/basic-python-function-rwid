list_word = ["abc","def","ghi"]

try:
    data = list_word[3]
    print(data)
except IndexError:
    print("Salah woey indexnya cuman 0 - 2")
