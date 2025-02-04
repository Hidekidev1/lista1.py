contar_letras = lambda lista: reduce(lambda x, y: x + y, map(len, lista))

print(contar_letras(["casa", "python", "lambda"]))  # Saída: 16
