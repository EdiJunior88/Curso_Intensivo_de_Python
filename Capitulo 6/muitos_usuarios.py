"""
Na listagem a seguir, armazenamos três informações sobre cada usuário:
seu primeiro nome, o sobrenome e a localidade. Acessaremos essas
informações percorrendo os nomes dos usuários em um laço e o dicionário
de informações associado a cada nome de usuário:
"""

usuarios = {
    'aeinstein': {
        'primeiro': 'albert',
        'último': 'einstein',
        'localização': 'princeton',
    },

    'mcurie': {
        'primeiro': 'marie',
        'último': 'curie',
        'localização': 'paris',
    },
}

for usuario_nome, usuario_info in usuarios.items():
    print("\nUsername: " + usuario_nome)
    nome_completo = usuario_info['primeiro'] + " " + usuario_info['último']
    localização = usuario_info['localização']

    print("\tNome Completo: " + nome_completo.title())
    print("\tLocalização: " + localização.title())