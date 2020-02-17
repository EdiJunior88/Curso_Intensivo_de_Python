"""
Para provar que realmente temos duas listas separadas, acrescentaremos
um alimento em cada lista e mostraremos que cada lista mantém um
registro apropriado das comidas favoritas de cada pessoa:
"""

minhas_comidas = ['pizza', 'falafel', 'carrot cake']
comida_amigo = minhas_comidas[:]

#acrescentando um alimento em cada lista
minhas_comidas.append('cannoli')
comida_amigo.append('ice cream')

print("Minhas comidas favoritas são:")
print(minhas_comidas)

print("\nAs comidas preferidas do meu amigo são:")
print(comida_amigo)