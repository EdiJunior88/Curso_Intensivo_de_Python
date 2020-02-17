"""
Você acabou de encontrar uma mesa de jantar maior portanto
agora tem mais espaço disponível. Pense em mais três convidados
para o jantar.

• Comece com seu programa do Exercício 3.4 ou do Exercício 3.5. Acrescente
uma instrução print no final de seu programa informando às pessoas que você
encontrou uma mesa de jantar maior.

• Utilize insert() para adicionar um novo convidado no início de sua lista.
• Utilize insert() para adicionar um novo convidado no meio de sua lista.
• Utilize append() para adicionar um novo convidado no final de sua lista.
• Exiba um novo conjunto de mensagens de convite, uma para cada pessoa que
está em sua lista.
"""

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
print("Oi " + nomes[6].title() + " venha jantar!")