"""
O exemplo anterior envolveu a armazenagem de diferentes tipos de
informação sobre um objeto: um alienígena em um jogo. Também
podemos usar um dicionário para armazenar um tipo de informação sobre
vários objetos.

Por exemplo, suponha que você queira fazer uma enquete
com várias pessoas e perguntar-lhes qual é a sua linguagem de
programação favorita. Um dicionário é conveniente para armazenar os
resultados de uma enquete simples, desta maneira:
"""

linguagem_favorita = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("A linguagem de programação favorita de Sarah é " + linguagem_favorita['sarah'].title() + ".")