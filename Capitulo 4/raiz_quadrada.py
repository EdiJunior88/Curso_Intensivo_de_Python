"""
Por exemplo, considere como criaríamos uma lista dos dez primeiros quadrados
perfeitos (isto é, o quadrado de cada inteiro de 1 a 10). Em Python, dois
asteriscos (**) representam exponenciais. Eis o modo como podemos colocar os
dez primeiros quadrados perfeitos em uma lista.
"""

raizes_quadradas = []
for valor in range(1,11):
    raiz_quadrada = valor ** 2
    raizes_quadradas.append(raiz_quadrada)

print(raizes_quadradas)

"""
Para escrever esse código de modo mais conciso, omita a variável
temporária square e concatene cada novo valor diretamente na lista:
"""

print()

raizes_quadradas = []
for valor in range(1,11):
    raizes_quadradas.append(valor**2)

print(raizes_quadradas)