filtrar_tuplas = lambda lista: list(filter(lambda t: sum(t) / len(t) > 5, lista))

print(filtrar_tuplas([(2, 8), (4, 5, 6), (1, 2)]))  # Saída: [(2, 8), (4, 5, 6)]
