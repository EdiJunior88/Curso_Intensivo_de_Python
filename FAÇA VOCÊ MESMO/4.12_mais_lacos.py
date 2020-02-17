"""
Todas as versões de foods.py nesta seção evitaram usar laços
for para fazer exibições a fim de economizar espaço. Escolha uma versão de
foods.py e escreva dois laços for para exibir cada lista de comidas.
"""

minhas_comidas = ['pizza', 'falafel', 'carrot cake']
comidas_amigo = minhas_comidas[:]

minhas_comidas.append('canolli')
comidas_amigo.append('ice cream')

print("Lista das minhas comidas:")
for minha_comida in minhas_comidas:
    print("-", minha_comida)

print("\nLista das comidas do meu amigo:")
for comida_amigo in comidas_amigo:
    print("-", comida_amigo)