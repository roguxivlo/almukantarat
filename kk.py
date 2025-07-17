czy_koniec = False

licznik_tury = 0

plansza = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]

# Dopóki czy_koniec jest False,
# czyli dopóki not czy_koniec jest True.
while True:
    # Tutaj gracze będą wykonywać ruchy:
    licznik_tury = licznik_tury + 1
    print("Tura")
    print(licznik_tury)

    znak = ""
    # Jeśli mamy nieparzystą turę, to jest kółko.
    # W przeciwnym przypadku - krzyżyk
    if licznik_tury % 2:
        znak = "o"
    else:
        znak = "x"

    # wczytaj ruch od gracza. To będą dwie liczby: wiersz i kolumna
    # oba numerowane od zera:
    wiersz = int(input("Podaj wiersz od 0 do 2"))
    kolumna = int(input("Podaj kolumne od 0 do 2"))

    # Sprawdzmy czy to pole jest wolne
    if plansza[wiersz][kolumna] != ".":
        print("Zagraj jeszcze raz na wolne pole!")
        licznik_tury = licznik_tury - 1
        # Kontynuuj pętle
        continue

    plansza[wiersz][kolumna] = znak

    # Wypisz nową planszę:
    print(plansza[0])
    print(plansza[1])
    print(plansza[2])

    # Teraz sprawdzamy czy ktoś wygrał:
    # Najpierw sprawdzamy wiersze:
    if plansza[0][0] == znak and plansza[0][1] == znak and plansza[0][2] == znak:
        print("Wygralo")
        print(znak)
        break
    if plansza[1][0] == znak and plansza[1][1] == znak and plansza[1][2] == znak:
        print("Wygralo")
        print(znak)
        break
    if plansza[2][0] == znak and plansza[2][1] == znak and plansza[2][2] == znak:
        print("Wygralo")
        print(znak)
        break

    # Teraz sprawdzamy kolumny:
    if plansza[0][0] == znak and plansza[1][0] == znak and plansza[2][0] == znak:
        print("Wygralo")
        print(znak)
        break
    if plansza[0][1] == znak and plansza[1][1] == znak and plansza[2][1] == znak:
        print("Wygralo")
        print(znak)
        break
    if plansza[0][2] == znak and plansza[1][2] == znak and plansza[2][2] == znak:
        print("Wygralo")
        print(znak)
        break

    # Teraz sprawdzamy przekątne:
    if plansza[0][0] == znak and plansza[1][1] == znak and plansza[2][2] == znak:
        print("Wygralo")
        print(znak)
        break
    if plansza[0][2] == znak and plansza[1][1] == znak and plansza[2][0] == znak:
        print("Wygralo")
        print(znak)
        break

    # Na koniec - trzeba sprawdzić remis.
    # Remis jest gdy wykonano 9 ruchów i nikt nie wygrał
    if licznik_tury == 9:
        print("Remis!")
        break
