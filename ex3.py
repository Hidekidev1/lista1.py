from functools import reduce

somar_lista = lambda lista: reduce(lambda x, y: x + y, lista)

print(somar_lista([1, 2, 3, 4]))  # Saída: 10
