array_data = [
    ["John", "Pria", 19, "lajang", "jakarta"],
    ["ean", "wanita", "21", "Menikah", "JaKarta"],
    ["TeRe", "Pria,", '25', "Menikah", "bandung"],
    ["May", "Wanita", 22, "menikah", "bandUng"]
]

# Menyeragamkan format data
for data in array_data:
    data[0] = data[0].capitalize()
    data[1] = data[1].capitalize()
    data[2] = int(data[2])
    data[3] = data[3].capitalize()
    data[4] = data[4].capitalize()

for data in array_data:
    print("Nama: {}, Kelamin: {}".format(data[0], data[1]), end='')
    print(", Usia:{}, Status : {}".format(data[2], data[3]), end='')
    print(", Kota: {}".format(data[4]))
