pares_impares = lambda lista: {
    "pares": list(filter(lambda x: x % 2 == 0, lista)),
    "ímpares": list(filter(lambda x: x % 2 != 0, lista))
}
print(pares_impares([1, 2, 3, 4, 5, 6]))  # Saída: {"pares": [2, 4, 6], "ímpares": [1, 3, 5]}
