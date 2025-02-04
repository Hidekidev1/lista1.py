from functools import reduce

def media_ponderada(alunos):
    return {
        nome: reduce(lambda x, y: x + y, notas[:-1]) / notas[-1]
        for nome, notas in alunos.items()
    }

entrada = {
    "João": [8, 7, 9, 2],  # Notas: [8, 7, 9], peso: 2
    "Ana": [5, 6, 7, 3]    # Notas: [5, 6, 7], peso: 3
}
saida = media_ponderada(entrada)
print(saida)  
