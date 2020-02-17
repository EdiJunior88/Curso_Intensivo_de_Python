"""
Na verdade, você pode usar pop() para remover um item de qualquer
posição em uma lista se incluir o índice do item que você deseja
remover entre parênteses.
"""

motos = ['honda', 'yamaha', 'suzuki']

primeira_moto = motos.pop(0)
print("A primeir moto que tive foi a " + primeira_moto.title() + ".")