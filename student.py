from statistics import mean
from typing import List


class Student:
    def __init__(self, imie, nazwisko, id):
        self.imie: str = imie
        self.nazwisko: str = nazwisko
        self.rok_urodzenia: int = 0
        self.pesel: int = 0
        self.id: int = id
        self.oceny: List[int] = [1, 3, 3]

    def dodaj_ocene(self, ocena: int):
        self.oceny.append(ocena)

    def pobierz_srednia_ocen(self):
        srednia_ocen = mean(self.oceny), 0
        return srednia_ocen