"""
Como podemos usar a função int() em um programa de verdade?
Considere um programa que determina se as pessoas têm altura suficiente
para andar em uma montanha-russa:
"""

altura = input("Qual é a sua altura em metros? ")
altura = int(altura)

if altura >= 100:
    print("\nVocê é alto o suficiente para ir no brinquedo!")
else:
    print("\nInfelizmente você não tem altura suficiente para ir no brinquedo.")