"""
Podemos fazer o programa parrot.py executar enquanto o usuário quiser
colocar a maior parte dele em um laço while. Definiremos um valor de
saída e então deixaremos o programa executando enquanto o usuário não
tiver fornecido o valor de saída:
"""

prompt = "\nMe diga uma coisa, e eu vou repetir de volta para você:"
prompt += "\nDigite 'quit' para sair do programa. "

mensagem = ""
while mensagem != 'quit':
    mensagem = input(prompt)
    print(mensagem)

