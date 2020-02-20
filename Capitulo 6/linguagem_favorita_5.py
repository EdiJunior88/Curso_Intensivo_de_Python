"""
Você também pode usar o método keys() para descobrir se uma pessoa
em particular participou da enquete. Dessa vez, vamos ver se Erin
respondeu à enquete:
"""

linguagem_favorita = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

if 'erin' not in linguagem_favorita:
    print("Erin, por favor, faça nossa enquete!")