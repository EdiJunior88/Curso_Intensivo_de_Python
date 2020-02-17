"""
Às vezes, você são saberá a posição do valor que quer
remover de uma lista. Se conhecer apenas o valor do
item que deseja remover, o método remove() poderá ser
usado.
"""

motos = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motos)

motos.remove('ducati')  #O código diz a Python para descobrir em que lugar 'ducati' aparece na lista e remover esse elemento
print(motos)