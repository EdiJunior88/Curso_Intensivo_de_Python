"""
Por exemplo, se tivermos um retângulo que sempre deva ter determinado
tamanho, podemos garantir que seu tamanho não mudará colocando as
dimensões em uma tupla
"""

dimensões = (200, 50)
print(dimensões[0])
print(dimensões[1])

dimensões[0] = 250 #Basicamente, pelo fato de estarmos tentando alterar uma tupla, o que não pode ser feito para esse tipo de objeto,

"""
Mensagem de erro:

Traceback (most recent call last):
  File "C:/Users/edivaldo.junior/Google Drive/Curso Intensivo de Python/Capitulo 4/dimensoes.py", line 11, in <module>
    dimensões[0] = 250
TypeError: 'tuple' object does not support item assignment
"""