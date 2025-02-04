def agrupar_numeros(lista):
    return {
        "positivos": list(filter(lambda x: x > 0, lista)),
        "negativos": list(filter(lambda x: x < 0, lista)),
        "zeros": list(filter(lambda x: x == 0, lista))
    }

entrada = [1, -2, 0, 3, -5, 0]
saida = agrupar_numeros(entrada)
print(saida)  
