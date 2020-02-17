"""
Escreva uma cadeia if-elif-else que determine o
estágio da vida de uma pessoa. Defina um valor para a variável age e então:

• Se a pessoa tiver menos de 2 anos de idade, mostre uma mensagem dizendo
que ela é um bebê.
• Se a pessoa tiver pelo menos 2 anos, mas menos de 4, mostre uma mensagem
dizendo que ela é uma criança.
• Se a pessoa tiver pelo menos 4 anos, mas menos de 13, mostre uma mensagem
dizendo que ela é um(a) garoto(a).
• Se a pessoa tiver pelo menos 13 anos, mas menos de 20, mostre uma
mensagem dizendo que ela é um(a) adolescente.
• Se a pessoa tiver pelo menos 20 anos, mas menos de 65, mostre uma
mensagem dizendo que ela é adulto.
• Se a pessoa tiver 65 anos ou mais, mostre uma mensagem dizendo que essa
pessoa é idoso
"""

idade = 20

if idade < 2:
    print("Você é um bebê!")
elif idade < 4:
    print("Você é uma criança!")
elif idade < 13:
    print("Você um garoto!")
elif idade < 20:
    print("Você é um adolescente!")
elif idade < 65:
    print("Você é um adulto!")
else:
    print("Você é idoso!")