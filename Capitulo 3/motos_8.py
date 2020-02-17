"""
Como esse método pop() poderia ser útil? Suponha que as motocicletas
da lista estejam armazenadas em ordem cronológica, de acordo com a
época em que fomos seus proprietários. Se for esse o caso, podemos usar o
método pop() para exibir uma afirmação sobre a última motocicleta que
compramos
"""

motos = ['honda', 'yamaha', 'suzuki']

última_moto = motos.pop()
print("A última que tive foi a " + última_moto.title() + ".")