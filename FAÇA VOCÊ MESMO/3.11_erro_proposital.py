"""
Se você ainda não recebeu um erro de índice em um de seus programas,
tente fazer um erro desse tipo acontecer. Altere um índice em um
de seus programas de modo a gerar um erro de índice. Não se esqueça
de corrigir o erro antes de fechar o programa.
"""

nomes = ['pedro', 'joão', 'thiago', 'junior']
print(len(nomes))
print(nomes[5]) #não existe o índice 5, pois só existem 4 componentes dessa lista


"""
mensagem de erro:
Traceback (most recent call last):
  File "C:/Users/edivaldo.junior/Google Drive/Curso Intensivo de Python/FAÇA VOCÊ MESMO/3.11_erro_proposital.py", line 9, in <module>
    print(nomes[5])
IndexError: list index out of range
"""