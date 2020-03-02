"""
Comece com o programa que você escreveu no Exercício 6.1 (página 147).
Crie dois novos dicionários que representem pessoas diferentes e
armazene os três dicionários em uma lista chamada people. Percorra sua lista de
pessoas com um laço. À medida que percorrer a lista, apresente tudo que você
sabe sobre cada pessoa
"""

#Faça uma lista vazia para armazenar pessoas.
pessoas = []

#Defina algumas pessoas e adicione-as à lista.
personalidade = {
    'primeiro nome': 'edivaldo',
    'ultimo nome': 'junior',
    'idade': 32,
    'cidade': 'maceió',
}
pessoas.append(personalidade)

personalidade = {
    'primeiro nome': 'amanda',
    'ultimo nome': 'larissa',
    'idade': 28,
    'cidade': 'são paulo',
}
pessoas.append(personalidade)

personalidade = {
    'primeiro nome': 'thaís',
    'ultimo nome': 'montes',
    'idade': 35,
    'cidade': 'recife',
}
pessoas.append(personalidade)

#Exibir todas as informações no dicionário.
for personalidade in pessoas:
    nome = personalidade['primeiro nome'].title() + " " + personalidade['ultimo nome'].title()
    idade = str(personalidade['idade'])
    cidade = personalidade['cidade'].title()

    print(nome + " da cidade de " + cidade + " com idade de " + idade + " anos.")

