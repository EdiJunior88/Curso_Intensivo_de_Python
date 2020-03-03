"""
Crie vários dicionários, em que o nome de cada
dicionário seja o nome de um animal de estimação. Em cada dicionário, inclua o
tipo do animal e o nome do dono. Armazene esses dicionários em uma lista
chamada pets. Em seguida, percorra sua lista com um laço e, à medida que fizer
isso, apresente tudo que você sabe sobre cada animal de estimaçã
"""

pets = []

animal = {
    'raca': 'cachorro',
    'nome do dono': 'tobi santos',
    'idade': 1,
}
pets.append(animal)

animal = {
    'raca': 'gato',
    'nome do dono': 'edivaldo junior',
    'idade': 10,
}
pets.append(animal)

for animal in pets:
    raça = animal['raca'].title()
    nome = animal['nome do dono'].title()
    idade = str(animal['idade'])

    print("Tipo de animal: " + raça)
    print("Nome do dono: " + nome)
    print("Idade do animal: " + idade + " ano(s)" + "\n")