"""
Para preservar a ordem original de uma lista, mas apresentá-la de forma
ordenada, podemos usar a função sorted(). A função sorted() permite
exibir sua lista em uma ordem em particular, mas não afeta a ordem
propriamente dita da lista.
"""

carros = ['bmw','audi','toyota','subaru']
print("Essa é a lista original:")
print(carros)

print("\nEssa é a lista sorteada:")
print(sorted(carros))

print("\nEssa é a lista original de novo:")
print(carros)