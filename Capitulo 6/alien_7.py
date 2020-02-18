"""
Quando não houver mais necessidade de uma informação armazenada em
um dicionário, podemos usar a instrução del para remover totalmente um
par chave-valor. Tudo de que del precisa é do nome do dicionário e da
chave que você deseja remover.

Por exemplo, vamos remover a chave 'points' do dicionário alien_0,
juntamente com seu valor
"""

alien_0 = {'color': 'green', 'pontuação': 5}
print(alien_0)

del alien_0['pontuação']
print(alien_0)