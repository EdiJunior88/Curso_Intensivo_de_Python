"""
Escreva um programa que pergunte ao usuário quantas pessoas estão
em seu grupo para jantar. Se a resposta for maior que oito,
exiba uma mensagem dizendo que eles deverão esperar uma mesa. Caso
contrário, informe que sua mesa está pronta.
"""

mensagem = int(input("Quantas pessoas no seu grupo irão jantar: "))

if mensagem > 8:
    print("Aguardem uma mesa disponível..")
else:
    print("Sua mesa está pronta!")