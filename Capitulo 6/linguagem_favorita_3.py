"""
O método keys() é conveniente quando não precisamos trabalhar com
todos os valores de um dicionário. Vamos percorrer o dicionário
favorite_languages com um laço e exibir os nomes de todos que
responderam à enquete:
"""

linguagem_favorita = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for nome in linguagem_favorita.keys():
    print(nome.title())