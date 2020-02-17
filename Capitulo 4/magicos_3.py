"""
Vamos acrescentar uma segunda linha em nossa mensagem, informando
a cada mágico que estamos ansiosos para ver o seu próximo truque:
"""

mágicos = ['alice', 'david', 'carolina']
for mágico in mágicos:
    print(mágico.title() + ", isso foi um ótimo truque!")
    print("Mal posso esperar para ver seu próximo truque, " + mágico.title() + ".\n")