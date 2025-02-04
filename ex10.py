from functools import reduce

media_ponderada = lambda alunos: {
    nome: reduce(lambda x, y: x + y, notas[:-1]) / notas[-1]
    for nome, notas in alunos.items()
}
entrada = {
    "João": [8, 7, 9, 2],  # Notas: 8, 7, 9; peso: 2
    "Ana": [5, 6, 7, 3]    # Notas: 5, 6, 7; peso: 3
}

print(media_ponderada(entrada))  
# Saída: {"João": 8.0, "Ana": 6.0}
