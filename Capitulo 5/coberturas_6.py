"""
Como exemplo, vamos verificar se a lista de ingredientes solicitados está
vazia antes de prepararmos a pizza. Se a lista estiver vazia, perguntaremos
ao usuário se ele realmente quer uma pizza simples. Se a lista não estiver
vazia, prepararemos a pizza exatamente como fizemos nos exemplos
anteriores:
"""

pedido_cobertura = []

if pedido_cobertura:
    for pedidos_coberturas in pedido_cobertura:
        print("Adicionando " + pedidos_coberturas + ".")
    print("\nTermiando de fazer a sua pizza!")
else:
    print("Tem certeza de que quer uma pizza simples?")