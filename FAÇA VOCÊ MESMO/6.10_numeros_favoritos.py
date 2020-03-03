"""
Modifique o seu programa do Exercício 6.2 (página
147) para que cada pessoa possa ter mais de um número favorito. Em seguida,
apresente o nome de cada pessoa, juntamente com seus números favoritos
"""

numeros_favoritos = {
    'cléber': [50, 49],
    'junior': [26, 100],
    'amanda': [1, 65],
    'cássia': [13, 1],
    'érica': [20, 15],
}

for nome, numero_favorito in numeros_favoritos.items():
    print(nome.title() + " gosta dos seguintes números:")
    for numero in numero_favorito:
       print("\t" + str(numero))
    print()