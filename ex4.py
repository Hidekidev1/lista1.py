def filtrar_nomes_longos(lista):
    return list(filter(lambda nome: len(nome) > 5, lista))

entrada = ["Ana", "Lucas", "Fernanda", "João"]
saida = filtrar_nomes_longos(entrada)
print(saida)  
