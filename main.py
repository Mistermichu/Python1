poprawnosc_danych = False

while poprawnosc_danych == False:

    kredyt = None
    while not isinstance(kredyt, float):
        try:
            kredyt = input("Wprowadz kwote kredytu: ")
            kredyt = float(kredyt)
        except ValueError:
            print("Podana wartosc nie jest liczba!")

    oprocentowanie = None
    while not isinstance(oprocentowanie, float):
        try:
            oprocentowanie = input("Wprowadz wartosc oprocentowania: ")
            oprocentowanie = float(oprocentowanie)
        except ValueError:
            print("Podana wartosc nie jest liczba!")

    kwota_raty = None
    while not isinstance(kwota_raty, float):
        try:
            kwota_raty = input("Wprowadz stala kwote raty: ")
            kwota_raty = float(kwota_raty)
        except ValueError:
            print("Podana wartosc nie jest liczba!")

    print("Potwierdz poprawnosc wprowadzonych danych")
    print(
        f"Kwota kredytu: {kredyt}, Oprocentowanie: {oprocentowanie}%, Kwota raty: {kwota_raty}")
    print("Czy podane wartosci sa poprawne?")
    print("Tak - wprowadz: Y")
    print("Nie - wprowadz: N")

    if input("").upper() == "Y":
        poprawnosc_danych = True
    else:
        poprawnosc_danych = False


print("Koniec programu")
