poprawnosc_danych = False

while poprawnosc_danych == False:

    kredyt = input("Wprowadz kwote kredytu: ")
    kredyt = float(kredyt)
    oprocentowanie = input("Wprowadz wartosc oprocentowania: ")
    oprocentowanie = float(oprocentowanie)
    kwota_raty = input("Wprowadz stala kwote raty: ")
    kwota_raty = float(kwota_raty)

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
