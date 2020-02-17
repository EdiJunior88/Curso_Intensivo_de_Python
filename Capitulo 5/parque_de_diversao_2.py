"""
Podemos usar quantos blocos elif quisermos em nosso código. Por
exemplo, se o parque de diversões implementasse um desconto para
idosos, você poderia acrescentar mais um teste condicional no código a fim
de determinar se uma pessoa está qualificada a receber esse desconto.
Suponha que qualquer pessoa com 65 anos ou mais pague metade do
preço normal da entrada, isto é, 5 dólares:
"""

idade = 12

if idade < 4:
    preco = 0
elif idade < 18:
    preco = 5
elif idade < 65:
    preco = 10
else:
    preco = 5

print("Seu ingresso custa R$" + str(preco))