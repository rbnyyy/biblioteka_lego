import csv

def plik_csv():
    try:
        with open("biblioteka_lego.csv", mode="r") as csvfile:
            reader = csv.DictReader(csvfile)
            for column in reader:
                numer_zestawu = column['numer_zestawu']
                ilosc_elementow = column['ilosc_elementow']
                cena_lego = float(column['cena_lego'])
                biblioteka_lego[numer_zestawu] = {'numer_zestawu': numer_zestawu, 'ilosc_elementow': ilosc_elementow, 'cena_lego': cena_lego}
    except FileNotFoundError:
        print("Nowy plik utworzony")

def czynnosci():
    plik_csv()
    print("Co chcesz zrobić?")
    print("Dodać zestaw - D")
    print("Usunąć zestaw - U")
    print("Przeglądać bibliotekę zestawów - P")
    print("Zapisać dodane zestawy do bazy CSV - Z")
    print("Wyłącz program bazy LEGO - X")
    wybor = input().lower()
    if wybor == "d":
        dodaj_nowy_zestaw()
    elif wybor == "u":
        usuwanie_zestawu()
    elif wybor == "p":
        przeglad_biblioteki()
    elif wybor == "z":
        zapis_zestawu_do_pliku_csv()
    elif wybor == "x":
        while True:
            print("Zamykam program bazy LEGO.")
            break

def dodaj_nowy_zestaw():
    global numer_zestawu
    numer_zestawu = input("Podaj numer zestawu: ")
    ilosc_elementow = input("Podaj ilość elementów: ")
    cena_lego = float(input("Podaj cenę zestawu za jaką go kupiłeś: "))
    biblioteka_lego[numer_zestawu] = {'numer_zestawu': numer_zestawu, 'ilosc_elementow': ilosc_elementow, 'cena_lego': cena_lego}
    print("Dodano nowy zestaw do biblioteki.")
    czynnosci()

def usuwanie_zestawu():
    usun_zestaw = input("Podaj numer zestawu do usunięcia: ")
    if usun_zestaw in biblioteka_lego:
        del biblioteka_lego[usun_zestaw]
        print("Usunięto zestaw z Twojej biblioteki")
    else:
        print("Nie ma podanego zestawu w bazie.")
    czynnosci()

def przeglad_biblioteki():
    print("Poniżej przedstawiam twoją bazę zestawów LEGO:")
    for numer_zestawu, zestaw in biblioteka_lego.items():
        print(numer_zestawu, zestaw)
    czynnosci()

def zapis_zestawu_do_pliku_csv():
    with open("biblioteka_lego.csv", mode="w", newline='') as csvfile:
        fieldnames = ['numer_zestawu', 'ilosc_elementow', 'cena_lego']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for zestaw in biblioteka_lego.values():
            writer.writerow(zestaw)
    print("Zapisano numer zestawu do bazy danych.")
    czynnosci()

biblioteka_lego = {}

czynnosci()
