from math import pi


def rounder(nilai):
    """
    Membulatkan nilai desimal sampai x karakter di belakang koma.
    x telah ditetapkan dalam script.

    :param nilai:Nilai angka yang ingin dibulatkan.
    :returns: Nilai angka yang telah dibulatkan
    """
    return round(nilai, 2)


def jari_ke_luas(nilai):
    """
    Penghitung luas lingkaran jika diketahui nilai jari-jari.

    :param  nilai: int atau float. Nilai jari-jari yang diketahui.
    :returns: Nilai luas lingkaran
    """

    return rounder(pi*(nilai**2))


def jari_ke_keliling(nilai):
    """
    Penghitung keliling lingkaran jika diketahui nilai jari-jari.

    :param nilai:int atau float. Nilai jari-jari yang diketahui
    :returns: Nilai keliling lingkaran
    """
    return rounder(pi*2*nilai)


def keliling_ke_jari(nilai):
    """
    Penghitung nilai jari-jari jika diketahui nilai keliling.

    :param nilai:int atau float. Nilai keliling yang diketahui.
    :returns: Nilai jari-jari lingkaran
    """
    return rounder(nilai/(2*pi))


def luas_to_jari(nilai):
    """
    Penghitung nilai jari-jari jika diketahui nilai luas.

    :param nilai:int atau float. Nilai luas yang diketahui.
    :return: Nilai jari-jari lingkaran
    """
    return rounder((nilai/pi)**0.5)
