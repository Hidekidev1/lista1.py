filtrar_pares = lambda lista: list(filter(lambda x: x % 2 == 0, lista))

print(filtrar_pares([1, 2, 3, 4, 5]))  # Saída: [2, 4]
