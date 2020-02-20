"""
Podemos acessar qualquer informação única sobre user_0 com base no
que já aprendemos neste capítulo. E se quiséssemos ver tudo que está
armazenado no dicionário desse usuário? Para isso, podemos percorrer o
dicionário com um laço for:
"""

user_0 = {
    'username': 'efermi',
    'primeiro': 'enrico',
    'último': 'fermi',
}

for key, value in user_0.items():
    print("Chave:", key)
    print("Valor:", value, "\n")