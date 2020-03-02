"""
Um exemplo mais realista envolveria mais de três alienígenas, com um
código que gere automaticamente cada alienígena. No exemplo a seguir,
usamos range() para criar uma frota de 30 alienígenas:
"""
#Cria uma lista vazia para armazenar alienígenas
aliens = []

#Cria 30 alienígenas verdes
for alien_number in range(0, 30):
    new_alien = {'cor': 'verde', 'pontos': '5', 'velocidade': 'lenta'}
    aliens.append(new_alien)

#Mostra os 5 primeiros alienígenas
for alien in aliens[:5]:
    print(alien)
print("...")

#Mostra quantos alienígenas foram criados
print("Total de número de alienígenas: " + str(len(aliens)))