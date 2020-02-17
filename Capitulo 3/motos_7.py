"""
Às vezes, você vai querer usar o valor de um item depois de removê-lo de
uma lista. O método pop() remove o último item de uma lista, mas permite que
você trabalhe com esse item depois da remoção. O termo pop deriva de
pensar em uma lista como se fosse uma pilha de itens e remover um item
(fazer um pop) do topo da pilha.
"""

motos = ['honda', 'yamaha', 'suzuki']
print(motos)

popped_motos = motos.pop() #fazemos pop de um valor da lista e o armazenamos na variável popped_motorcycle
print(motos) #Exibimos a lista para mostrar que um valor foi removido da lista
print(popped_motos) #exibimos o valor removido para provar que ainda temos acesso ao valor removido