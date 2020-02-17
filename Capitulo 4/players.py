"""
Como ocorre na função range(), Python para em um item antes  do segundo índice
que você especificar. Para exibir os três primeiros elementos de uma lista,
solicite os índices de 0 a 3; os elementos 0, 1 e 2 serão devolvidos
"""
players = ['charles', 'martina', 'michael', 'florence', 'eli',]
print(players[0:3])
print(players[1:4])

"""
Se o primeiro índice de uma fatia for omitido, Python começará sua fatia
automaticamente no início da lista
"""
print(players[:4])

"""
Uma sintaxe semelhante funcionará se você quiser uma fatia que inclua o
final de uma lista. Por exemplo, se quiser todos os itens do terceiro até o
último item, podemos começar com o índice 2 e omitir o segundo índice
"""
print(players[2:])

"""
Por exemplo, se quisermos apresentar os três últimos jogadores da lista, 
podemos usar a fatia players[-3:]:
"""
print(players[-3:])