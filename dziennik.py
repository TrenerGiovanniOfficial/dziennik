from typing import List

from student import Student




class Dziennik:
    def __init__(self, rok, litera):
        self._rok_szkolny = rok
        self._ktora_klasa_litera = litera
        self._uczniowie: List[Student] = []

    def podaj_ilosc_studentow(self) -> int:
        ilosc_studentow = len(self._uczniowie)
        return ilosc_studentow

    def dodaj_studenta(self, imie, nazwisko):
        id = self._generuj_id()
        s = Student(imie, nazwisko, id)
        self._uczniowie.append(s)

    def pobierz_studenta(self, id: int) -> Student:
        for uczen in self._uczniowie:
            if uczen.id == id:
                return uczen

    def _generuj_id(self) -> int:
        nowy_id = len(self._uczniowie) + 1
        print(nowy_id)
        return nowy_id

