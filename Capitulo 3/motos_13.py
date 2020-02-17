"""
Tenha em mente que, sempre que quiser acessar o último item de uma
lista, você deve usar o índice -1. Isso sempre funcionará, mesmo que sua
lista tenha mudado de tamanho desde a última vez que você a acessou:
"""

motos = ['honda', 'yamaha', 'suzuki']
print(motos[-1])

print("-----------------------------------")

motos = []
print(motos[-1])

"""
A única ocasião em que essa abordagem causará um erro é quando
solicitamos o último item de uma lista vazia:

mensagem de erro:
  File "C:/Users/edivaldo.junior/Google Drive/Curso Intensivo de Python/Capitulo 3/motos_13.py", line 13, in <module>
-----------------------------------
    print(motos[-1])
IndexError: list index out of range
"""