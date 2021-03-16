def ciag(a=1, b=4, ile=10):
    for x in range(ile):
        a = a * b
    return a


print("Iloczyn elementow ciagu wynosi: ", ciag())
print("Iloczyn elementow ciagu wynosi: ", ciag(1, 2, 5))
