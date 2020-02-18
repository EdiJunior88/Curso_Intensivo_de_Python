"""
Vamos adicionar duas novas informações ao dicionário alien_0: as
coordenadas x e y do alienígena, que nos ajudarão a exibir o alienígena em
determinada posição da tela. Vamos colocar o alienígena na borda
esquerda da tela, 25 pixels abaixo da margem superior.

Como as coordenadas da tela normalmente começam no canto superior esquerdo da
tela, posicionaremos o alienígena na margem esquerda definindo a
coordenada x com 0, e 25 pixels abaixo da margem superior, definindo a
coordenada y com o valor 25 positivo, como vemos aqui
"""

alien_0 = {'cor': 'verde', 'pontuação': 5}
print(alien_0)

alien_0['x_posição'] = 0
alien_0['y_posição'] = 25
print(alien_0)