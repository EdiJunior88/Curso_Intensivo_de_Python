"""
Para modificar um valor em um dicionário, especifique o nome do
dicionário com a chave entre colchetes e o novo valor que você quer
associar a essa chave. Por exemplo, considere um alienígena que muda de
verde para amarelo à medida que o jogo prossegue:
"""

alien_0 = {'x_posição': 0, 'y_posição': 5, 'velocidade': 'médio'}
print("Original x-posição: " + str(alien_0['x_posição']))

#Move o alienígena para a direita
#Determina a distância que o alienígena deve se deslocar de acordo com sua velocidade atual

if alien_0['velocidade'] == 'lento':
    x_increment = 1
elif alien_0['velocidade'] == 'médio':
    x_increment = 2
else:
    #Este deve ser um alienígena rápido
    x_increment = 3

#A nova posição é a posição antiga somada ao incremento
alien_0['x_posição'] = alien_0['x_posição'] + x_increment

print("Nova x-posição: " + str(alien_0['x_posição']))