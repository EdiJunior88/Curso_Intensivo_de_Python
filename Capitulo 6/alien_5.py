"""
Para modificar um valor em um dicionário, especifique o nome do
dicionário com a chave entre colchetes e o novo valor que você quer
associar a essa chave. Por exemplo, considere um alienígena que muda de
verde para amarelo à medida que o jogo prossegue:
"""

alien_0 = {'cor': 'verde'}
print("O alien é " + alien_0['cor'] + ".")

alien_0['cor'] = 'amarelo'
print("O alien agora é " + alien_0['cor'] + ".")