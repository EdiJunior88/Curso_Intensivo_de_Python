"""
Trabalhando com um dos programas dos Exercícios de 3.4 a 3.7 (páginas 80 e 81),
use len() para exibir uma mensagem informando o número de pessoas que você está
convidando para o jantar.
"""
#Programa Lista de Convidados exercício 3.6
#lista de nomes
nomes = ['jhon', 'fernanda', 'isaac', 'bruna', 'alex']

#excluindo um nome da lista .pop(), porém, ainda posso usá-lo no programa
nome_excluido = nomes.pop(1)
print("Infelizmente o(a) " + nome_excluido.title() + " não poderá vir!")

#nova lista de nomes aparecendo na tela
print("\nOi " + nomes[0].title() + " venha jantar!")
print("Oi " + nomes[1].title() + " venha jantar!")
print("Oi " + nomes[2].title() + " venha jantar!")
print("Oi " + nomes[3].title() + " venha jantar!")
print("\nConsegui encontrar uma mesa maior!")

#adicionando um novo nome no início da lista
nomes.insert(0, 'ruan')

#adicionando um novo nome no meio da lista
nomes.insert(3, 'giovana')

#adicionando um novo nome no final da lista
nomes.append('flávio')

#eibindo novos nomes da lista de convidados
print("\nOi " + nomes[0].title() + " venha jantar!")
print("Oi " + nomes[1].title() + " venha jantar!")
print("Oi " + nomes[2].title() + " venha jantar!")
print("Oi " + nomes[3].title() + " venha jantar!")
print("Oi " + nomes[4].title() + " venha jantar!")
print("Oi " + nomes[5].title() + " venha jantar!")
print("Oi " + nomes[6].title() + " venha jantar!\n")

print("Quantidades de convidados: " + str(len(nomes)))