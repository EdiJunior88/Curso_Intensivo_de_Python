"""
Esse código não funcionaria de modo apropriado se tivéssemos usado um
bloco if-elif-else, pois o código pararia de executar depois que apenas um
teste tivesse passado. Esse código seria assim:
"""

pedido_cobertura = ['cogumelos', 'queijo extra']

if 'cogumelos' in pedido_cobertura:
    print("Adicionando cogumelos.")
elif 'pepproni' in pedido_cobertura:
    print("Adicionando pepperoni.")
elif 'queijo extra' in pedido_cobertura:
    print("Adicionando queijo extra.")

print("\nTerminou de fazer sua pizza!")