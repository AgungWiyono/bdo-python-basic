array_data = [
    ["John", "Pria", 19, "lajang", "jakarta"],
    ["Jean", "wanita", "21", "Menikah", "JaKarta"],
    ["TeRe", "Pria,", '25', "Menikah", "bandung"],
    ["May", "Wanita", 22, "menikah", "bandUng"]
]


def formatter(data):
    result = []
    for column in range(len(data)):
        if column == 2:
            result.append(int(data[column]))
        else:
            result.append(data[column].capitalize())
    return result


def show_data(array_data):
    header = ["Nama", "Kelamin", "Usia", "Status", "Kota"]
    for data in array_data:
        for number, content in enumerate(data):
            print("{}: {}, ".format(header[number], content), end='')
        print('')


show_data(list(map(formatter, array_data)))
