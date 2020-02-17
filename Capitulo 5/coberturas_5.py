"""
Vamos prosseguir com o exemplo da pizzaria. A pizzaria exibe uma
mensagem sempre que um ingrediente é adicionado à sua pizza à medida
que ela é preparada. O código para essa ação pode ser escrito de modo
bem eficiente se criarmos uma lista de ingredientes solicitados pelo
cliente e usarmos um laço para anunciar cada ingrediente à medida que
ele é acrescentado à pizza:
"""

"""
pedido_cobertura = ['cogumelos', 'pimentão verde', 'queijo extra']

for pedidos_coberturas in pedido_cobertura:
    print("Adicionando " + pedidos_coberturas + ".")

print("\nTerminou de fazer a sua pizza!")
"""

"""
E se a pizzaria ficasse sem pimentões verdes? Uma instrução if no laço
for pode tratar essa situação de modo apropriado:
"""

pedido_cobertura = ['cogumelos', 'pimentão verde', 'queijo extra']

for pedidos_coberturas in pedido_cobertura:
    if pedidos_coberturas == 'pimentão verde':
        print("Desculpe, estamos sem pimentão verde agora.")
    else:
        print("Adicionando " + pedidos_coberturas + ".")

print("\nTerminou de fazer a sua pizza!")