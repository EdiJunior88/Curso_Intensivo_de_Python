"""
Crie uma lista chamada sandwich_orders e a preencha com os
nomes de vários sanduíches. Em seguida, crie uma lista vazia chamada
finished_sandwiches. Percorra a lista de pedidos de sanduíches com um laço e
mostre uma mensagem para cada pedido, por exemplo, Preparei seu sanduíche
de atum. À medida que cada sanduíche for preparado, transfira-o para a lista de
sanduíches prontos. Depois que todos os sanduíches estiverem prontos, mostre uma
mensagem que liste cada sanduíche preparado
"""

lista_sanduiches = ['atum', 'queijo', 'mortandela', 'presunto']

sanduiches_terminados = []

while lista_sanduiches:
    pedido_sanduiche = lista_sanduiches.pop()
    print("Estou fazendo o seu sanduíche de " + pedido_sanduiche)
    sanduiches_terminados.append(pedido_sanduiche)

print("\n")
for sanduiche in sanduiches_terminados:
    print("O seu sanduíche de " + sanduiche + " está pronto.")