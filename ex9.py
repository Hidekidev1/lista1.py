def filtrar_tuplas(lista):
    return list(filter(lambda t: sum(t) / len(t) > 5, lista))

entrada = [(2, 8), (4, 5, 6), (1, 2)]
saida = filtrar_tuplas(entrada)
print(saida)  
