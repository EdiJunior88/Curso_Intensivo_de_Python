"""
Peça um número ao usuário e, em seguida, informe se o
número é múltiplo de dez ou não.
"""

número = int(input("Digite um número: "))

if número % 10 == 0:
    print(str(número) + " é multiplo de 10")
else:
    print(str(número) + " não é multiplo de 10")