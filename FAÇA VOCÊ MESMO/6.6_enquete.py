"""
Utilize o código em favorite_languages.py (página 150).

• Crie uma lista de pessoas que devam participar da enquete sobre linguagem
favorita. Inclua alguns nomes que já estejam no dicionário e outros que não
estão.
• Percorra a lista de pessoas que devem participar da enquete. Se elas já tiverem
respondido à enquete, mostre uma mensagem agradecendo-lhes por responder.

Se ainda não participaram da enquete, apresente uma mensagem convidando-as
a responder.
"""

linguagem_favorita = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'andressa': 'javascript',
    'edivaldo': 'c#',
}

pessoas_fora_da_enquete = ['edivaldo', 'andressa']

for nome, linguagem in linguagem_favorita.items():
    print("A linguagem de programação favorita de " + nome.title() + " é " + linguagem +".")

print()

for nome in linguagem_favorita:
    if nome in pessoas_fora_da_enquete: #Lista os itens que estão em um array 'edivaldo' e 'andressa'
        print(nome.title() + ", por favor, faça nossa enquete!")
    else:
        print(nome.title() + ", obrigado por participar da enquete.")

