"""
Podemos acessar o valor associado a qualquer chave que nos interessar
no laço usando a chave atual. Vamos exibir uma mensagem a dois amigos
sobre as linguagens que eles escolheram. Percorreremos os nomes no
dicionário com um laço como fizemos antes, porém, quando o nome for de
um de nossos amigos, apresentaremos uma mensagem sobre sua
linguagem favorita:
"""

linguagem_favorita = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

amigos = ['phil', 'sarah']

for nome in linguagem_favorita.keys():
    print(nome.title())

    if nome in amigos:
        print(" Olá", nome.title() + ", Eu vejo que você gosta da linguagem de programação", linguagem_favorita[nome].title() + "!")