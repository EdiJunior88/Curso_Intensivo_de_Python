"""
Também podemos usar a função range() para dizer a Python que ignore
alguns números em um dado intervalo. Por exemplo, eis o modo de listar
os números pares entre 1 e 10.

Nesse exemplo, a função range() começa com o valor 2 e então soma 2 a
esse valor. O valor 2 é somado repetidamente até o valor final, que é 11,
ser alcançado ou ultrapassado, e o resultado a seguir é gerado
"""

ate_numeros = list(range(2,11,2))
print(ate_numeros)