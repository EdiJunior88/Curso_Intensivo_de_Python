"""
Às vezes, é importante verificar se uma lista contém um determinado valor
antes de executar uma ação. Por exemplo, talvez você queira verificar se
um novo nome de usuário já existe em uma lista de nomes de usuários
atuais antes de concluir o registro de alguém em um site. Em um projeto de
mapeamento, você pode querer verificar se uma localidade submetida já
existe em uma lista de localidades conhecidas.

Criaremos uma lista de ingredientes que um cliente pediu em sua pizza e,
então, verificaremos se determinados ingredientes estão na lista.
"""

pedido_cobertura = ['cogumelos', 'cebolas', 'abacaxi']

print('cogumelos' in pedido_cobertura)
print('pepperoni' in pedido_cobertura)