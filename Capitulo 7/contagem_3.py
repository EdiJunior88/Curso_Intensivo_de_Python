"""
Todo laço while precisa de uma maneira de interromper a execução para
que não continue executando indefinidamente. Por exemplo, o laço a
seguir deve fazer a contagem de 1 a 5:

Contudo, se você omitir a linha x += 1 (como vemos a seguir) por
acidente, o laço executará para sempre:
"""

x = 1
while x <= 5:
    print(x)
    #x += 1 #Se omitir essa linha o laço executará para sempre!
