"""
Para ver cada linguagem escolhida sem repetições, podemos usar
um conjunto (set). Um conjunto é semelhante a uma lista, exceto
que cada item de um conjunto deve ser único:
"""

linguagem_favorita = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("As seguintes linguagens foram mencionadas:")

for linguagem in set(linguagem_favorita.values()):
    print(linguagem.title())