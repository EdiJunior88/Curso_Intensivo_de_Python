"""
Como podemos trabalhar com um conjunto de alienígenas como esse?
Suponha que um aspecto do jogo consista em fazer alguns alienígenas
mudarem de cor e moverem-se mais rápido à medida que o jogo
prosseguir. Quando for o momento de mudar de cor, podemos usar um
laço for e uma instrução if para alterar a cor dos alienígenas. Por exemplo,
para mudar os três primeiros alienígenas para amarelo, com velocidade
média, valendo dez pontos cada, podemos fazer o seguinte:
"""

#Cria uma lista vazia para armazenar alienígenas
aliens = []

#Cria 30 alienígenas verdes
for alien_number in range(0, 30):
    new_alien = {'cor': 'verde', 'pontos': '5', 'velocidade': 'lenta'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['cor'] == 'verde':
        alien['cor'] = 'amarelo'
        alien['velocidade'] = 'médio'
        alien['pontos'] = 10

#Mostra os 5 primeiros alienígenas
for alien in aliens[:5]:
    print(alien)
print("...")