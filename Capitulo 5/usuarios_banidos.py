"""
Em outras ocasiões, é importante saber se um valor não está em uma lista.
Podemos usar a palavra reservada not nesse caso. Por exemplo, considere
uma lista de usuários que foi impedida de fazer comentários em um fórum.
Podemos verificar se um usuário foi banido antes de permitir que essa
pessoa submeta um comentário:
"""

usuarios_banidos = ['andrew', 'carolina', 'david']
usuario = 'marie'

if usuario not in usuarios_banidos:
    print(usuario.title() + ", você pode postar uma resposta, se desejar.")