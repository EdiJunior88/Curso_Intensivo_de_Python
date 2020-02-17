"""
Uma list comprehension (abrangência de lista) permite gerar essa mesma
lista com apenas uma linha de código. Uma list comprehension combina o
laço for e a criação de novos elementos em uma linha, e concatena cada
novo elemento automaticamente.
"""

raiz_quadrada = [valor**2 for valor in range(1,11)]
print(raiz_quadrada)