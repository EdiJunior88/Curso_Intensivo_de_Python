"""
Um cinema cobra preços diferentes para os
ingressos de acordo com a idade de uma pessoa. Se uma pessoa tiver menos de 3
anos de idade, o ingresso será gratuito; se tiver entre 3 e 12 anos, o ingresso
custará 10 dólares; se tiver mais de 12 anos, o ingresso custará 15 dólares.

Escreva um laço em que você pergunte a idade aos usuários e, então, informe-lhes
o preço do ingresso do cinema
"""
print("Preço do Ingresso do Parque de Diversões")
print("*****************************************")
print("Digite quit para finalizar o programa:")
print("*****************************************")

idade = int(input("\nDigite a sua idade: "))

if int(idade) < 3:
    print("Ingresso gratuito.")
elif int(idade) <= 12:
    print("Preço do Ingresso: R$ 10,00")
else:
    print("Preço do Ingresso: R$ 15,00")