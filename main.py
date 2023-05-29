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

# inflacja_rok_miesiac

inflacja_1_styczen = 1.592824484
inflacja_1_luty = -0.453509101
inflacja_1_marzec = 2.324671717
inflacja_1_kwiecien = 1.261254407
inflacja_1_maj = 1.782526286
inflacja_1_czerwiec = 2.329384541
inflacja_1_lipiec = 1.502229842
inflacja_1_sierpien = 1.782526286
inflacja_1_wrzesien = 2.328848994
inflacja_1_pazdziernik = 0.616921348
inflacja_1_listopad = 2, 352295886
inflacja_1_grudzien = 0.337779545
inflacja_2_styczen = 1.577035247
inflacja_2_luty = -0.292781443
inflacja_2_marzec = 2.48619659
inflacja_2_kwiecien = 0.267110318
inflacja_2_maj = 1.417952672
inflacja_2_czerwiec = 1.054243267
inflacja_2_lipiec = 1.480520104
inflacja_2_sierpien = 1.577035247
inflacja_2_wrzesien = -0.07742069
inflacja_2_pazdziernik = 1.165733399
inflacja_2_listopad = -0.404186718
inflacja_2_grudzien = 1.499708521


print("Koniec programu")
