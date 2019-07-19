def print_judul(text):
    print(text.upper())
    print('='* len(text))

def print_isi(daftar_isi):
    for nomor, isi in enumerate(daftar_isi):
        print("{}. {}".format(nomor, isi.title()))

def main_processor(data):
    for content in data:
        print(content['judul'])
        print(content['isi'])

draft = [
            {
                'judul' : 'bagian satu - pengenalan',
                'isi' : ['pengenalan python', 'aplikasi python di kehidupan']
            },
            {
                'judul' : 'bagian dua - pembahasan dasar',
                'isi' : ['variabel', 'tipe data di python']
            },
            {
                'judul' : 'bagian tiga - perulangan',
                'isi' : ['for statement', 'while statement']
            }
]
main_processor(draft)
