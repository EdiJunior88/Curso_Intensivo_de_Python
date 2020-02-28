"""
Uma maneira de fazer os itens serem devolvidos em determinada
sequência é ordenar as chaves à medida que são devolvidas no laço for.
Podemos usar a função sorted() para obter uma cópia ordenada das
chaves:
"""

linguagem_favorita = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for nome in sorted(linguagem_favorita.keys()):
    print(nome.title() + ", obrigado por participar da enquete.")