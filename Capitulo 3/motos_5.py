"""
Com frequência, você vai querer remover um item
ou um conjunto de itens de uma lista. Você pode
remover um item de acordo com sua posição na
lista ou seu valor.

Se a posição do item que você quer remover de
uma lista for conhecida, a instrução del poderá
ser usada.
"""

motos = ['honda', 'yamaha', 'suzuki']
print(motos)

del motos[0] #O código usa del para remover o primeiro item, 'honda', da lista de motocicletas
print(motos)