"""
Python não exige um bloco else no final de uma cadeia if-elif. Às vezes,
um bloco else é útil; outras vezes, é mais claro usar uma instrução elif
adicional que capture a condição específica de interesse:
"""

idade = 12

if idade < 4:
    preco = 0
elif idade < 18:
    preco = 5
elif idade < 65:
    preco = 10
elif idade >= 65:
    preco = 5

print("Seu ingresso custa R$" + str(preco))