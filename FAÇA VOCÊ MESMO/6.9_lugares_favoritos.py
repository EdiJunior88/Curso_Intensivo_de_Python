"""
Crie um dicionário chamado favorite_places. Pense em
três nomes para usar como chaves do dicionário e armazene de um a três lugares
favoritos para cada pessoa. Para deixar este exercício um pouco mais interessante,
peça a alguns amigos que nomeiem alguns de seus lugares favoritos. Percorra o
dicionário com um laço e apresente o nome de cada pessoa e seus lugares
favoritos.
"""

lugar_favorito = {
    'lourdes': ['itália', 'são paulo', 'israel'],
    'edivaldo junior': ['são paulo', 'japão', 'rússia'],
    'iraí': ['são paulo', 'itália', 'alemanha'],
}

for nomes, lugares in lugar_favorito.items():
    print("O lugares favoritos de " + nomes.title() + " são:")
    for lugar in lugares:
        print("- " + lugar.title())
    print()