"""
Esse programa funciona bem, exceto que exibe a palavra 'quit' como se
fosse uma mensagem de verdade. Um teste if simples corrige esse
problema:
"""

prompt = "\nMe diga uma coisa, e eu vou repetir de volta para você:"
prompt += "\nDigite 'quit' para sair do programa. "

mensagem = ""
while mensagem != 'quit':
    mensagem = input(prompt)

    if mensagem != 'quit':
        print(mensagem)
