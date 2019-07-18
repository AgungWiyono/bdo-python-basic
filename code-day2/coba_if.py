kondisi = True
angka = 12

while kondisi:
    tebak = input("Tebak sebuah angka : ")

    if not tebak.isdigit():
        print("Anda tidak memasukkan bilangan bulat yang valid.")
        print("Silahkan ulangi lagi.")
    elif tebak > angka:
        print("Tebakan anda terlalu besar.")
    elif tebak < angka:
        print("Tebakan anda terlalu kecil.")   
    else :
        print("Selamat tebakan anda benar.")
        kondisi = False
