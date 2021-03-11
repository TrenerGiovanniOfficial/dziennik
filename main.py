from dziennik import Dziennik

dziennik = Dziennik(rok=2021, litera="c")
dziennik.dodaj_studenta(imie="Jan", nazwisko="Kowalski")
dziennik.dodaj_studenta(imie='Marek', nazwisko="Nowak")

student = dziennik.pobierz_studenta(2)
print(student.pobierz_srednia_ocen())
# print(dziennik.podaj_ilosc_studentow())
