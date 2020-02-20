"""
Percorrer todos os pares chave-valor com um laço funciona bem, em
particular, para dicionários como o do exemplo em favorite_languages.py,
que armazena o mesmo tipo de informação para várias chaves diferentes.

Se percorrermos o dicionário favorite_languages com um laço, teremos o
nome de cada pessoa no dicionário e sua linguagem de programação
favorita. Como as chaves sempre se referem ao nome de uma pessoa e o
valor é sempre uma linguagem, usaremos as variáveis name e language no
laço, em vez de key e value. Isso facilita entender o que está acontecendo:
"""

linguagem_favorita = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for nome, linguagem in linguagem_favorita.items():
    print("A linguagem favorita de", nome.title(), "é", linguagem.title() + ".")