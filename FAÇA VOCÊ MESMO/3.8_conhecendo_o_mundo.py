"""
Pense em pelo menos cinco lugares do mundo que
você gostaria de visitar.

• Armazene as localidades em uma lista. Certifique-se de que a lista não esteja em
ordem alfabética.
• Exiba sua lista na ordem original. Não se preocupe em exibir a lista de forma
elegante; basta exibi-la como uma lista Python pura.
• Utilize sorted() para exibir sua lista em ordem alfabética, sem modificar a lista
propriamente dita.
• Mostre que sua lista manteve sua ordem original exibindo-a.
• Utilize sorted() para exibir sua lista em ordem alfabética inversa sem alterar a
ordem da lista original.
• Mostre que sua lista manteve sua ordem original exibindo-a novamente.
• Utilize reverse() para mudar a ordem de sua lista. Exiba a lista para mostrar
que sua ordem mudou.
• Utilize reverse() para mudar a ordem de sua lista novamente. Exiba a lista para
mostrar que ela voltou à sua ordem original.
• Utilize sort() para mudar sua lista de modo que ela seja armazenada em
ordem alfabética. Exiba a lista para mostrar que sua ordem mudou.
• Utilize sort() para mudar sua lista de modo que ela seja armazenada em
ordem alfabética inversa. Exiba a lista para mostrar que sua ordem mudou.
"""

cidades = ['são paulo', 'maceió', 'rio de janeiro', 'amazonas']

print("Lista de cidades:")
print(cidades)

print("-----------------------------------------------------")

print("Exibir a lista em ordem alfabética, sem modificá-la: sorted()")
print(sorted(cidades))

print("-----------------------------------------------------")

print("Lista de cidades:")
print(cidades)

print("-----------------------------------------------------")

print("Exibir a Lista em ordem alfabética inversa sem modificá-la: sorted()")
print(sorted(cidades, reverse=True))

print("-----------------------------------------------------")

print("Lista de cidades:")
print(cidades)

print("-----------------------------------------------------")

print("Mudando a ordem da lista: reverse()")
cidades.reverse()
print(cidades)

print("-----------------------------------------------------")

print("Lista de cidades:")
print(cidades)

print("-----------------------------------------------------")

print("Mudando novamente a ordem da lista: reverse()")
cidades.reverse()
print(cidades)

print("-----------------------------------------------------")

print("Lista de cidades:")
print(cidades)

print("-----------------------------------------------------")

print("Lista armazenada em ordem alfabética: sort()")
cidades.sort()
print(cidades)

print("-----------------------------------------------------")

print("Lista de cidades:")
print(cidades)

print("-----------------------------------------------------")

print("Lista armazenada em ordem alfabética inversa: sort()")
cidades.sort(reverse=True)
print(cidades)

print("-----------------------------------------------------")

print("Lista de cidades:")
print(cidades)