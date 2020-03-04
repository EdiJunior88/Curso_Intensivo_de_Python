"""
Para sair de um laço while de imediato, sem executar qualquer código
restante no laço, independentemente do resultado de qualquer teste
condicional, utilize a instrução break. A instrução break direciona o fluxo
de seu programa; podemos usá-la para controlar quais linhas de código são
ou não são executadas, de modo que o programa execute apenas o código
que você quiser, quando você quiser.

Por exemplo, considere um programa que pergunte aos usuários os
nomes de lugares que eles já visitaram. Podemos interromper o laço while
nesse programa chamando break assim que o usuário fornecer o valor
'quit':
"""

prompt = "\nDigite o nome da cidade que você visitou recentemente: "
prompt += "\n(Digite 'quit' para sair do programa.) "

while True:
    cidade = input(prompt)

    if cidade == 'quit':
        break
    else:
        print("Eu amo viajar para a(o) " + cidade.title() + "!")