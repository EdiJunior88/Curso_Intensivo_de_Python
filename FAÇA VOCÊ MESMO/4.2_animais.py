"""
Pense em pelo menos três animais diferentes que tenham uma característica em comum.
Armazene os nomes desses animais em uma lista e, então, utilize um laço for para
exibir o nome de cada animal.

• Modifique seu programa para exibir uma frase sobre cada animal, por exemplo,
Um cachorro seria um ótimo animal de estimação.

• Acrescente uma linha no final de seu programa informando o que esses animais
têm em comum. Você poderia exibir uma frase como Qualquer um desses animais seria
um ótimo animal de estimação!
"""

animais = ['gato', 'cachorro', 'coelho']
for animal in animais:
    print(animal)

print()

for animal in animais:
    print("Um " + animal + " seria ótimo como animal de estimação.")

print("\nQualquer um desses animais seria um ótimo anima de estimação!")