"""
O código a seguir percorre uma lista de nomes de carros em
um laço e procura o valor 'bmw'. Sempre que o valor for 'bmw',
ele será exibido com letras maiúsculas, e não apenas com a
inicial maiúscula
"""

carros = ['audi', 'bmw', 'subaru', 'toyota']

for carro in carros:
    if carro == 'bmw':
        print(carro.upper())
    else:
        print(carro.title())