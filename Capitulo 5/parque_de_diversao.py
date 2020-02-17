"""
Por exemplo, considere um parque de diversões que cobre
preços distintos para grupos etários diferentes:

• a entrada para qualquer pessoa com menos de 4 anos é gratuita;
• a entrada para qualquer pessoa com idade entre 4 e 18 anos custa 5
dólares;
• a entrada para qualquer pessoa com 18 anos ou mais custa 10 dólares.

Como podemos usar uma instrução if para determinar o preço da
entrada de alguém? O código a seguir testa a faixa etária de uma pessoa e
então exibe uma mensagem com o preço da entrada:
"""

idade = 12
if idade < 4:
    print("Seu ingresso custa R$0.00")
elif idade < 18:
    print("Seu ingresso custa R$5.00")
else:
    print("Seu ingresso custa R$10.00")

"""
Em vez de exibir o preço da entrada no bloco if-elif-else, seria mais
conciso apenas definir o preço na cadeia if-elif-else e, então, ter uma
instrução print simples que execute depois que a cadeia for avaliada:
"""

idade = 12

if idade < 4:
    preco = 0.00
elif idade < 18:
    preco = 5.00
else:
    preco = 10.00

print("Seu ingresso custa R$" + str(preco))