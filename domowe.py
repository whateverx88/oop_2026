# napis = "Ala ma kota"
# print(napis)
# print(type(2))
#
# print(napis.count("a"))
# print(len(napis))
#
# print(napis.split(" "))
#
# lista = [1,2,3,4,5]
# print(type(lista))
# print(dir(napis))
# print(dir(lista))

imie = input("Dzien dobry. Podaj swoje imie: ")
print(f"Witaj {imie}. Milo Cie widziec. Teraz podaj swoj wiek")
while True:
    wiek = input("Moj wiek to: ")
    try:
        wiek_int = int(wiek)
        if wiek_int >= 120:
            raise SystemError("AAAAAA")
        elif wiek_int < 1:
            raise SystemError
        break
    except SystemError:
        print("Podany wiek jest za maly lub za duzy")
    except ValueError:
        print("Podaj wlasciwy wiek")
        continue
    else:
        print("Inny blad")
    # finally:
    #     print("Skonczylem obsluge bledow")
