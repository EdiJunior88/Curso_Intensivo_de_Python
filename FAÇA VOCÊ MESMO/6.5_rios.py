"""
Crie um dicionário que contenha três rios importantes e o país que
cada rio corta. Um par chave-valor poderia ser 'nilo': 'egito'.

• Use um laço para exibir uma frase sobre cada rio, por exemplo, O Nilo corre
pelo Egito.
• Use um laço para exibir o nome de cada rio incluído no dicionário.
• Use um laço para exibir o nome de cada país incluído no dicionário
"""

rios = {
    'amazonas': 'brasil',
    'yangtzé': 'china',
    'nilo': 'egito',
}

país = ['yangtzé']

print("Principais rios do mundo e seus países:")

for rio in rios.keys():
    print("Rio: " + rio.title() + " --- País: " + rios[rio].title())

print()

for frase in rios.keys():
    if frase in país:  #Uilizei o IF() para que o print mude o "corre pela" por causa da palavra china
        print("O rio " + frase.title() + " corre pela " + rios[frase].title())
    else:
        print("O rio " + frase.title() + " corre pelo " + rios[frase].title())
