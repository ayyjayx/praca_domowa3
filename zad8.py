def zakupy(** rzeczy):
    suma = 0
    ilosc = 0
    cena = [cena for cena in rzeczy.values()]
    for x in range(len(cena)):
        suma += cena[x]
        ilosc += 1
    print("Ilosc produktow wynosi: ", ilosc)
    return suma


print(zakupy(baton=2, woda=3, cola=30, chleb=2, mleko=4))
