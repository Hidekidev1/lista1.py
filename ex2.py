def filtrar_pares(lista):
    return list(filter(lambda x: x % 2 == 0, lista))

entrada = [1, 2, 3, 4, 5]
saida = filtrar_pares(entrada)
print(saida)  
