filtrar_nomes_longos = lambda lista: list(filter(lambda nome: len(nome) > 5, lista))

print(filtrar_nomes_longos(["Ana", "Lucas", "Fernanda", "João"]))  # Saída: ["Lucas", "Fernanda"]
