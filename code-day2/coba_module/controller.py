from rumus_base import (jari_ke_luas, jari_ke_keliling,
                        keliling_ke_jari, luas_to_jari)


def penghitung_luas(nilai, jenis):
    """
    Penghitung luas dengan nilai dari jari-jari, keliling atau diameter.

    :param nilai: int atau float dari nilai yang diketahui
    :param jenis: str. Jenis nilai input, r(jari-jari), d(diameter), k(keliling)
    :returns: Nilai luas
    """

    if jenis == 'r':
        return jari_ke_luas(nilai)
    elif jenis == 'l':
        return jari_ke_luas(d/2)
    else:
        return jari_ke_luas(keliling_ke_jari(nilai))


def penghitung_jari_jari(nilai, jenis):
    """
    Penghitung jari-jari dengan nilai diameter, keliling atau luas.

    :param nilai: int atau float dari nilai yang diketahui
    :param jenis: str. Jenis nilai input, d(diameter), k(keliling), l(luas)
    :returns: Nilai jari-jari
    """

    if jenis == 'd':
        return nilai/2
    elif jenis == 'l':
        return luas_to_jari(nilai)
    else:
        return keliling_ke_jari(nilai)


def penghitung_keliling(nilai, jenis):
    """
    Penghitung keliling dengan nilai jari-jari, diameter, atau luas.

    :param nilai: int atau float dari nilai yang diketahui
    :param jenis: str. Jenis nilai input, r(jari-jari), d(diameter), l(luas)
    :returns: Nilai keliling
    """

    if jenis == 'r':
        return jari_ke_keliling(nilai)
    elif jenis == 'd':
        return jari_ke_keliling(nilai/2)
    else:
        return jari_ke_keliling(luas_to_jari(nilai))


def penghitung_diameter(nilai, jenis):
    """
    Penghitung diameter dengan nilai jari-jari, diameter, atau luas.

    :param nilai: int atau float dari nilai yang diketahui
    :param jenis: str. Jenis nilai yang diketahui, r(jari-jari), k(keliling), l(luas)
    """

    if jenis == 'r':
        return nilai*2
    elif jenis == 'k':
        return keliling_ke_jari(nilai)*2
    else:
        return luas_to_jari(nilai)*2
