"""
Agora que você já sabe como percorrer um dicionário com um
laço, limpe o código do Exercício 6.3 (página 148), substituindo sua sequência de
instruções print por um laço que percorra as chaves e os valores do dicionário.
Quando tiver certeza de que seu laço funciona, acrescente mais cinco termos de
Python ao seu glossário. Ao executar seu programa novamente, essas palavras e
significados novos deverão ser automaticamente incluídos na saída.
"""

glossário = {
    'print()': 'imprimir caracateres na tela',
    'input()': 'entrada de caracteres através do teclado',
    'bool()': 'retorna valores em booleano',
    'len()': 'verifica a quantidade de caracteres',
    'pow()': 'retorna o valor de uma raiz quadrada',
    'while()': 'um conjunto de instruções seja executado enquanto uma condição é atendida',
    'for()': 'é utilizado para a iteração através de uma sequência',
    'int()': 'constrói um número inteiro a partir de um literal inteiro',
    'float()': 'constrói um número ponto flutuante a partir de um literal inteiro',
    'str()': 'constrói uma string a partir de uma ampla variedade de tipos de dados',
}

for comandos in glossário.keys():
    print("Palavra: " + comandos + " //// Significado: " + glossário[comandos])