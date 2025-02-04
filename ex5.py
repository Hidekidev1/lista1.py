def elevar_quadrado_e_ordenar(lista):
    return sorted(map(lambda x: x ** 2, lista))

entrada = [3, 1, 4, 2]
saida = elevar_quadrado_e_ordenar(entrada)
print(saida)  
