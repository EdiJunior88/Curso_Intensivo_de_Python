"""
Se você estiver mais interessado nos valores contidos em um dicionário, o
método values() pode ser usado para devolver uma lista de valores sem as
chaves. Por exemplo, suponha que queremos apenas uma lista de todas as
linguagens escolhidas em nossa enquete sobre linguagens de programação,
sem o nome da pessoa que escolheu cada linguagem.
"""

linguagem_favorita = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

print("As seguintes linguagens foram mencionadas:")

for linguagem in linguagem_favorita.values():
    print(linguagem.title())