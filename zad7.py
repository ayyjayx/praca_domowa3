def ciag(* elementy):
    a = 1
    for x in range(len(elementy)):
        a *= elementy[x]
    return a


print("Iloczyn elementow ciagu wynosi: ", ciag(2, 3, 6, 9, 12))
