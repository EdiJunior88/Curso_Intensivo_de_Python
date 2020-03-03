"""
O operador de módulo não diz quantas vezes um número cabe em outro;
ele simplesmente informa o resto.

Quando um número é divisível por outro, o resto é 0, portanto o
operador de módulo sempre devolve 0 nesse caso. Podemos usar esse fato
para determinar se um número é par ou ímpar:
"""

número = input("Digite um número, e eu vou te dizer se é par ou ímpar: ")
número = int(número)

if número % 2 == 0:
    print("\nO número " + str(número) + " é PAR.")
else:
    print("\nO número " + str(número) + " é ÍMPAR.")