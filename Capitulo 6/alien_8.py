"""
Como podemos administrar uma frota de alienígenas?
Uma maneira é criar uma lista de alienígenas, em que
cada alienígena seja representado por um dicionário com informações
sobre ele. Por exemplo, o código a seguir cria uma lista com três
alienígenas:
"""

alien_0 = {'cor': 'verde', 'pontos': '5'}
alien_1 = {'cor': 'amarelo', 'pontos': '10'}
alien_2 = {'cor': 'vermelho', 'pontos': '15'}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)