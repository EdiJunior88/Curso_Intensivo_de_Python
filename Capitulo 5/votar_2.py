"""
Exibiremos a mesma mensagem mostrada antes se a pessoa tiver idade
suficiente para votar, porém, desta vez, acrescentaremos uma mensagem
para qualquer um que não tenha idade suficiente para votar:
"""

idade = 17
if idade >= 18:
    print("Você tem idade suficiente para votar!")
    print("Você já se registrou para votar?")
else:
    print("Desculpe, você é jovem demais para votar.")
    print("Registre-se para votar assim que completar 18 anos!")