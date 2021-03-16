import random
lista_a = []
for x in range (10):
    lista_a.append(random.randint(0, 1000))
print(lista_a)
a = [a for a in lista_a if a % 2 == 0]
print(a)
