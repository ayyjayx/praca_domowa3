from math import *
def prostokatny(a, b, c):
    if a > 0 and b > 0 and c > 0:
        if pow(a, 2) + pow(b, 2) == pow(c, 2):
            print("Trojkat jest prostokatny")
            return 1
        elif pow(a, 2) + pow(c, 2) == pow(b, 2):
            print("Trojkat jest prostokatny")
            return 1
        elif pow(b, 2) + pow(c, 2) == pow(a, 2):
            print("Trojkat jest prostokatny")
            return 1
        else:
            print("Trojkat nie jest prostokatny")
            return 0
    else:
        print("Podano bledne wartosci")
        return -1
print(prostokatny(3, 4, 5))
print(prostokatny(5, 3, 4))
print(prostokatny(3, 5, 4))
print(prostokatny(1, 1, 1))
print(prostokatny(-2, 3, 5))
