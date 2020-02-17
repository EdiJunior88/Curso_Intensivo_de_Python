"""
Um tipo de erro é comum quando trabalhamos com listas pela primeira
vez. Suponha que temos uma lista com três itens e você solicite o quarto
item:
"""

"""
Por causa da natureza deslocada de um na indexação de listas, esse erro 
é característico. As pessoas acham que o terceiro item é o item de número 3, 
pois começam a contar a partir de 1. Contudo, em Python, o terceiro item 
é o de número 2, pois a indexação começa em 0.
"""

motos = ['honda', 'yamaha', 'suzuki']
print(motos[3])

"""
Mensagem de erro: 
Traceback (most recent call last):
  File "C:/Users/edivaldo.junior/Google Drive/Curso Intensivo de Python/Capitulo 3/motos_12.py", line 8, in <module>
    print(motos[3])
IndexError: list index out of range
"""