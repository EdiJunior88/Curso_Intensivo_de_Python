"""
O exemplo a seguir define duas listas. A primeira é uma lista de ingredientes
disponíveis na pizzaria, e a segunda é a lista de ingredientes que o usuário
pediu. Dessa vez, cada item em requested_toppings é verificado em relação à
lista de ingredientes disponíveis antes de ser adicionado à pizza:
"""

cobertura_disponivel = ['cogumelos', 'azeitonas', 'pimentão verde', 'pepperoni', 'abacaxi', 'queijo extra']

pedido_cobertura = ['cogumelos', 'batatas fritas', 'queijo extra']

for pedidos_coberturas in pedido_cobertura:
    if pedidos_coberturas in cobertura_disponivel:
        print("Adicionando " + pedidos_coberturas + ".")
    else:
        print("Desculpe, nós não temos " + pedidos_coberturas + ".")

print("\nTerminando de fazer a sua pizza!")