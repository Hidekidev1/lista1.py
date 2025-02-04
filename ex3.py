from functools import reduce

def somar_lista(lista):
    return reduce(lambda x, y: x + y, lista)

entrada = [1, 2, 3, 4]
saida = somar_lista(entrada)
print(saida)  
