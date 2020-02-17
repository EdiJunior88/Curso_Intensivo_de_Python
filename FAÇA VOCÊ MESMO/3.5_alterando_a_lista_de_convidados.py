"""
Você acabou de saber que um de seus convidados não poderá
comparecer ao jantar, portanto será necessário enviar um
novo conjunto de convites. Você deverá pensar em outra
pessoa para convidar
"""

#lista de nomes
nomes = ['jhon', 'fernanda', 'isaac', 'bruna', 'alex']

#excluindo um nome da lista
print("Infelizmente o(a) " + nomes[1].title() + " não poderá vir!")
del nomes[1]

#nova lista de nomes aparecendo na tela
print("\nOi " + nomes[0].title() + " venha jantar!")
print("Oi " + nomes[1].title() + " venha jantar!")
print("Oi " + nomes[2].title() + " venha jantar!")
print("Oi " + nomes[3].title() + " venha jantar!")