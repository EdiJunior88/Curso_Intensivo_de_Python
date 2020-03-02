"""
Você pode aninhar uma lista em um dicionário sempre que quiser que
mais de um valor seja associado a uma única chave em um dicionário. No
exemplo anterior das linguagens de programação favoritas, se
armazenássemos as respostas de cada pessoa em uma lista, elas poderiam
escolher mais de uma linguagem predileta. Se percorrermos o dicionário
com um laço, o valor associado a cada pessoa será uma lista das
linguagens, e não uma única linguagem. No laço for do dicionário, usamos
outro laço for para percorrer a lista de linguagens associada a cada pessoa:
"""

linguagens_favoritas = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskel'],
}

for nome, linguagens in linguagens_favoritas.items():
    print("\n" + "A linguagem favorita de " + nome.title() + " é:")
    for linguagem in linguagens:
        print("\t" + linguagem.title())