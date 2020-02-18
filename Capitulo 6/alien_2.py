"""
Agora podemos acessar a cor ou o valor da pontuação de alien_0. Se um
jogador atingir esse alienígena, podemos consultar quantos pontos ele deve
ganhar usando um código como este:
"""

alien_0 = {'cor': 'verde', 'pontuação': 5}

nova_pontuação = alien_0['pontuação']

print("Você acabou de ganhar " + str(nova_pontuação) + " pontos!")