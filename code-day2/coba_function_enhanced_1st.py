def print_judul(text):
    print(text.upper())
    print('=' * len(text))
def print_isi(daftar_isi):
    for nomor, isi in enumerate(daftar_isi):
        print("{}. {}".format(nomor, isi.title()))

# Sekarang kita akan membuat tampilan seperti script sebelumnya
#  dengan menggunakan 2 fungsi diatas
print_judul('bagian satu - pengenalan')
print_isi(['pengenalan python', 'aplikasi python di kehidupan nyata', 'siapa saja'])
print_judul('bagian dua - pembahasan dasar')
print_isi(['variabel', 'tipe data di python'])
print_judul('bagian tiga - perulangan')
print_isi(['for statement', 'while statement'])
