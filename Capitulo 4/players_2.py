"""
No próximo exemplo, percorreremos os três primeiros jogadores
e exibiremos seus nomes como parte de uma lista simples:
"""

players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Aqui estão os três primeiros jogadores do meu time:")

for player in players[:3]:
    print(player.title())