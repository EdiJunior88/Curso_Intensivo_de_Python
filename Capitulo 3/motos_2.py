"""
A maneira mais simples de acrescentar um novo elemento em uma lista é
concatenar o item na lista. Quando concatenamos um item em uma lista, o
novo elemento é acrescentado no final. Usando a mesma lista que
tínhamos no exemplo anterior, adicionaremos o novo elemento 'ducati
"""

motos = ['honda', 'yamaha', 'suzuki']
print(motos)

motos.append('ducati') #O método append() acrescenta 'ducati' no final da lista sem afetar qualquer outro elemento
print(motos)