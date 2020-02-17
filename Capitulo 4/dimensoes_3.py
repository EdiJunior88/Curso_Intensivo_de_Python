"""
Embora não seja possível modificar uma tupla, podemos atribuir um novo
valor a uma variável que armazena uma tupla. Portanto, se quiséssemos
alterar nossas dimensões, poderíamos redefinir a tupla toda:
"""

dimensões = (200, 50)
print("Dimensões Originais:")
for dimensão in dimensões:
    print(dimensão)

dimensões = (400, 100)
print("\nModificando as dimensões:")
for dimensão in dimensões:
    print(dimensão)