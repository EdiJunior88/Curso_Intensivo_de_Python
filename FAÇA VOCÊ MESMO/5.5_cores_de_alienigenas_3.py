"""
Transforme sua cadeia if-else do Exercício 5.4
em uma cadeia if-elif-else.

• Se o alienígena for verde, mostre uma mensagem informando que o jogador
ganhou cinco pontos.
• Se o alienígena for amarelo, mostre uma mensagem informando que o jogador
ganhou dez pontos.
• Se o alienígena for vermelho, mostre uma mensagem informando que o jogador
ganhou quinze pontos.
• Escreva três versões desse programa, garantindo que cada mensagem seja
exibida para a cor apropriada do alienígena.
"""

alien_color = 'vermelho'

if alien_color == 'verde':
    print("Você ganhou 5 pontos!")
elif alien_color == 'amarelo':
    print("Você ganhou 10 pontos!")
elif alien_color == 'vermelho':
    print("Você ganhou 15 pontos!")
else:
    print("Você ganhou 5 pontos!")