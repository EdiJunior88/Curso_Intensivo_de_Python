"""
Pensa em algo que você poderia armazenar em uma lista. Por exemplo,
você poderia criar uma lista de montanhas, rios, países, cidades,
idiomas ou qualquer outro item que quiser. Escreva um programa que
crie uma lista contendo esses itens e então utilize cada função
apresentada neste capítulo pelo menos uma vez.
"""

países = ['itália', 'alemanha', 'nova zelândia', 'frança', 'brasil', 'estados unidos']

países_2 = ['itália', 'alemanha', 'nova zelândia', 'frança', 'brasil', 'estados unidos']
países_2.sort()

países_3 = ['itália', 'alemanha', 'nova zelândia', 'frança', 'brasil', 'estados unidos']
países_3.sort(reverse=True)

países_4 = ['itália', 'alemanha', 'nova zelândia', 'frança', 'brasil', 'estados unidos']
países_4.reverse()

países_5 = ['itália', 'alemanha', 'nova zelândia', 'frança', 'brasil', 'estados unidos']
países_5.append('ucrânia')

países_6 = ['itália', 'alemanha', 'nova zelândia', 'frança', 'brasil', 'estados unidos']
países_6.insert(0,'venezuela')

países_7 = ['itália', 'alemanha', 'nova zelândia', 'frança', 'brasil', 'estados unidos']
del países_7[1]

países_8 = ['itália', 'alemanha', 'nova zelândia', 'frança', 'brasil', 'estados unidos']
países_8.pop()

países_9 = ['itália', 'alemanha', 'nova zelândia', 'frança', 'brasil', 'estados unidos']
países_9.remove('brasil')

print("-----------------------------------------------------------------------------")
print("\t\t\t\t\t\t\tLISTA DE PAÍSES")
print(países) #mostra a lista "ARRAYS" de países
print("-----------------------------------------------------------------------------")
print(países[0].title()) #primeira letra em maiúsculo e mostra apenas o 2º item da lista
print(países_2) #armazena a lista em ordem alfabética
print(países_3) #armazena a lista em ordem alfabética invertida
print(sorted(países)) #exibe a lista em ordem alfabética, sem modificar a lista propriamente dita
print(países_4) #muda a ordem de uma lista de forma permanente
print("Quantidade de itens da lista: " + str(len(países))) #exibe o tamanho de uma lista
print(países_5) #acrescenta mais um item "ucrânia" na lista
print(países_6) #acrescenta um item "venezuela" no início da lista
print(países_7) #deleta permanentemente "alemanha" um item da lista
print(países_8) #remove o último item de uma lista, mas permite que você trabalhe com esse item depois da remoção
print(países_9) #remove um item específico da lista