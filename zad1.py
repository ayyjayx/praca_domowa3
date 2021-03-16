x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = [1 - x for x in x]
print(a)

b = [4 ** y for y in range (7)]
print(b)

c = [z for z in b if z % 2 == 0]
print(c)
