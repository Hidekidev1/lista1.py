agrupar_numeros = lambda lista: {
    "positivos": list(filter(lambda x: x > 0, lista)),
    "negativos": list(filter(lambda x: x < 0, lista)),
    "zeros": list(filter(lambda x: x == 0, lista))
}

print(agrupar_numeros([1, -2, 0, 3, -5, 0]))  # Saída: {"positivos": [1, 3], "negativos": [-2, -5], "zeros": [0, 0]}
