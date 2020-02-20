"""
Use um dicionário para armazenar informações sobre uma pessoa
que você conheça. Armazene seu primeiro nome, o sobrenome, a idade e a
cidade em que ela vive. Você deverá ter chaves como first_name, last_name,
age e city. Mostre cada informação armazenada em seu dicionário
"""

nomes = {
    'primeiro_nome': 'edivaldo',
    'ultimo_nome': 'junior',
    'idade': '30',
    'cidade': 'maceió',
}

print("Nome:", nomes['primeiro_nome'].title())
print("Sobrenome:", nomes['ultimo_nome'].title())
print("Idade:", nomes['idade'].title(), "anos")
print("Cidade:", nomes['cidade'].title())
