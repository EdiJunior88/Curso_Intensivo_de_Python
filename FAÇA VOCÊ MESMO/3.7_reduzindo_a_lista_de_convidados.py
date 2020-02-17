"""
Você acabou de descobrir que sua nova mesa de jantar não chegará a
tempo para o jantar e tem espaço para somente dois convidados.

Comece com seu programa do Exercício 3.6. Acrescente uma nova linha que
mostre uma mensagem informando que você pode convidar apenas duas pessoas
para o jantar.

• Utilize pop() para remover os convidados de sua lista, um de cada vez, até que
apenas dois nomes permaneçam em sua lista. Sempre que remover um nome de
sua lista, mostre uma mensagem a essa pessoa, permitindo que ela saiba que
você sente muito por não poder convidá-la para o jantar.
• Apresente uma mensagem para cada uma das duas pessoas que continuam na
lista, permitindo que elas saibam que ainda estão convidadas.
• Utilize del para remover os dois últimos nomes de sua lista, de modo que você
tenha uma lista vazia. Mostre sua lista para garantir que você realmente tem uma
lista vazia no final de seu programa.
"""

#lista de nomes
nomes = ['jhon', 'fernanda', 'isaac', 'bruna', 'alex']

#nova lista de nomes aparecendo na tela
print("Oi " + nomes[0].title() + " venha jantar!")
print("Oi " + nomes[1].title() + " venha jantar!")
print("Oi " + nomes[2].title() + " venha jantar!")
print("Oi " + nomes[3].title() + " venha jantar!")

#excluindo um nome da lista
print("\nInfelizmente a " + nomes[1].title() + " não poderá vir!")
del nomes[1]

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

print("\nPor contra-tempos só posso ter 2 pessoas no jantar!")

#uma variável para cada nome excluído
nome_excluido = nomes.pop()
nome_excluido1 = nomes.pop()
nome_excluido2 = nomes.pop()
nome_excluido3 = nomes.pop()
nome_excluido4 = nomes.pop()

#exibindo na tela os nomes excluídos
print("\nOlá " + nome_excluido.title() + " não posso convidá-lo(a) ao jantar!")
print("Olá " + nome_excluido1.title() + " não posso convidá-lo(a) ao jantar!")
print("Olá " + nome_excluido2.title() + " não posso convidá-lo(a) ao jantar!")
print("Olá " + nome_excluido3.title() + " não posso convidá-lo(a) ao jantar!")
print("Olá " + nome_excluido4.title() + " não posso convidá-lo(a) ao jantar!")

#exibindo na tela os nomes que estão sobrando
print("\nOlá " + nomes[0].title() + " você ainda está convidado para jantar!")
print("Olá " + nomes[1].title() + " você ainda está convidado para jantar!\n")

#excluindo permanentemente os 2 nomes que sobraram
del nomes[0]
del nomes[0]

#exibindo na tela a lista vazia
print(nomes)