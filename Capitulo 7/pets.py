"""
No Capítulo 3 usamos remove() para remover um valor específico de uma
lista. A função remove() era apropriada porque o valor em que estávamos
interessados aparecia apenas uma vez na lista. Porém, e se quiséssemos
remover da lista todas as instâncias de um valor?

Suponha que tenhamos uma lista de animais de estimação com o valor
'cat' repetido várias vezes. Para remover todas as instâncias desse valor,
podemos executar um laço while até 'cat' não estar mais na lista, como
vemos aqui:
"""

pets = ['cachorro', 'gato', 'cachorro', 'golfinho', 'gato', 'coelho', 'gato']
print(pets)

while 'gato' in pets:
    pets.remove('gato')

print(pets)