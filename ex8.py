from functools import reduce

def contar_letras(lista):
    return reduce(lambda x, y: x + y, map(len, lista))

entrada = ["casa", "python", "lambda"]
saida = contar_letras(entrada)
print(saida)  
