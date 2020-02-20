"""
Um dicionário Python pode ser usado para modelar um dicionário
de verdade. No entanto, para evitar confusão, vamos chamá-lo de glossário.

• Pense em cinco palavras relacionadas à programação que você conheceu nos
capítulos anteriores. Use essas palavras como chaves em seu glossário e
armazene seus significados como valores.

• Mostre cada palavra e seu significado em uma saída formatada de modo
elegante. Você pode exibir a palavra seguida de dois-pontos e depois o seu
significado, ou apresentar a palavra em uma linha e então exibir seu significado
indentado em uma segunda linha. Utilize o caractere de quebra de linha (\n)
para inserir uma linha em branco entre cada par palavra-significado em sua
saída
"""

glossário = {
    'palavra': 'print()', 'significado': 'imprimir caracateres na tela',
    'palavra1': 'input()', 'significado1': 'entrada de caracteres através do teclado',
    'palavra2': 'bool()', 'significado2': 'retorna valores em booleano',
    'palavra3': 'len()', 'significado3': 'verifica a quantidade de caracteres',
    'palavra4': 'pow()', 'significado4': 'retorna o valor de uma raiz quadrada',
}

print("Palavra:", glossário['palavra'], "//// Significado:", glossário['significado'])
print("Palavra:", glossário['palavra1'], "//// Significado:", glossário['significado1'])
print("Palavra:", glossário['palavra2'], "//// Significado:", glossário['significado2'])
print("Palavra:", glossário['palavra3'], "//// Significado:", glossário['significado3'])
print("Palavra:", glossário['palavra4'], "//// Significado:", glossário['significado4'])