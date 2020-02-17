"""
Por exemplo, eis o que acontece quando tentamos copiar uma lista sem usar uma fatia:
"""

minhas_comidas = ['pizza', 'falafel', 'carrot cake']

#Isto não funciona:
comida_amigo = minhas_comidas

minhas_comidas.append('cannoli')
comida_amigo.append('ice cream')

print("Minhas comidas favoritas são:")
print(minhas_comidas)

print("\nAs comidas favoritas do meu amigo são:")
print(comida_amigo)