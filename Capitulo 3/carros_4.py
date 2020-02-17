"""
ara inverter a ordem original de uma lista, podemos usar o método
reverse(). Se armazenarmos originalmente a lista de carros em ordem
cronológica, de acordo com a época em que fomos seus proprietários,
poderemos facilmente reorganizar a lista em ordem cronológica inversa.

O método reverse() muda a ordem de uma lista de forma permanente,
mas podemos restaurar a ordem original a qualquer momento aplicando
reverse() à mesma lista uma segunda vez.
"""

carros = ['bmw','audi','toyota','subaru']
print(carros)
carros.reverse()
print(carros)