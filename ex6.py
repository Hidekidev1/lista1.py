def pares_impares(lista):
    return {
        "pares": list(filter(lambda x: x % 2 == 0, lista)),
        "ímpares": list(filter(lambda x: x % 2 != 0, lista))
    }

entrada = [1, 2, 3, 4, 5, 6]
saida = pares_impares(entrada)
print(saida)  
