"""
Também podemos usar o método remove() para trabalhar com um valor
que está sendo removido de uma lista. Vamos remover o valor 'ducati' e
exibir um motivo para removê-lo da lista
"""

"""
NOTA: O método remove() apaga apenas a primeira ocorrência do valor que você
especificar. Se houver a possibilidade de o valor aparecer mais de uma vez na
lista, será necessário usar um laço para determinar se todas as ocorrências desse
valor foram removidas.
"""

motos = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motos)

muito_caro = 'ducati' #Armazenamos o valor 'ducati' em uma variável chamada too_expensive
motos.remove(muito_caro) #O valor 'ducati' foi removido da lista, mas continua armazenado na variável muito_caro
print(motos)
print("\nA " + muito_caro.title() + " é muito cara para mim.")