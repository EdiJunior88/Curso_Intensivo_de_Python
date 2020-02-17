"""
Por exemplo, suponha que temos uma lista de nossos alimentos
prediletos e queremos criar uma lista separada de comidas que
um amigo gosta. Esse amigo gosta de tudo que está em nossa lista
até agora, portanto podemos criar sua lista copiando a nossa
"""

minhas_comidas = ['pizza', 'falafel', 'carrot cake']
comida_amigo = minhas_comidas[:]

print("Minhas comidas favoritas são:")
print(minhas_comidas)

print("\nAs comidas preferidas do meu amigo são:")
print(comida_amigo)