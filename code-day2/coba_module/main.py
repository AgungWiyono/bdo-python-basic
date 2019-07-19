from controller import (penghitung_luas, penghitung_jari_jari,
                        penghitung_keliling, penghitung_diameter)


CHOICE_LIST = {
    'r' : [penghitung_jari_jari, 'Jari-Jari'],
    'd': [penghitung_diameter, 'Diameter'],
    'k': [penghitung_keliling, 'Keliling'],
    'l': [penghitung_luas, 'Luas']
}


def show_choices(choice_list=CHOICE_LIST.keys()):
    for number, element in enumerate(choice_list):
        print("{}. {}: {}".format(number + 1, element, CHOICE_LIST[element][1]))
    print('')


def get_choice(source_list=CHOICE_LIST.keys()):
    choice = input('Masukkan pilihan anda: ')
    print('')

    if choice == 'stop':
        return False

    if choice not in source_list:
        print("Pilihan anda salah.")
        return get_choice(source_list)
    else:
        return choice


def value_source(choice):
    temp = list(CHOICE_LIST.keys())
    temp.remove(choice)
    return temp


def main_script():
    while True:

        print("Apa yang ingin anda cari nilainya :")
        show_choices()

        print("Untuk berhenti ketikkan `stop'.")
        print('')

        target = get_choice()
        print('')

        if not target:
            break

        print("Masukkan elemen yang anda ketahui.")
        source = get_choice(value_source(target))

        if not source:
            break
        print('')
        value = int(input("Masukkan nilai yang diketahui : "))

        result = CHOICE_LIST[target][0](value, source)
        print('')
        print('Hasilnya adalah: {}'.format(result))
        print("="*30)
        print('\n'*2)
