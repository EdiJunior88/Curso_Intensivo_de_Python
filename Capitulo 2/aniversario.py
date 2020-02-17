"""
É um erro de tipo. Significa que Python não é capaz de reconhecer o tipo
de informação que você está usando. Nesse exemplo, Python vê que você
está usando uma variável cujo valor é um inteiro (int), mas não tem
certeza de como interpretar esse valor. O interpretador sabe que a variável
poderia representar um valor numérico 23 ou os caracteres 2 e 3.
"""

"""
idade = 23
mensagem = "Feliz " + idade + "º Aniversário!"

print(mensagem)
"""

idade = 23
mensagem = "Feliz " + str(idade) + "º Aniversário!"

print(mensagem)