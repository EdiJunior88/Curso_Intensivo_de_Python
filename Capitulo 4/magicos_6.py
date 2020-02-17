"""
Por exemplo, eis o que acontece quando nos esquecemos de indentar a
segunda linha do laço que diz a cada mágico que estamos ansiosos para
ver o seu próximo truque.

Como resultado, a primeira instrução print é executada uma vez para cada
nome da lista, pois está indentada. A segunda instrução print não está
indentada, portanto é executada somente uma vez, depois que o laço terminar
de executar. Como o valor final de magician é 'carolina', ela é a única
que recebe a mensagem de “ansiosos pelo próximo truque”:
"""

mágicos = ['alice', 'david', 'carolina']
for mágico in mágicos:
    print(mágico.title() + ", isso foi um bom truque!")
print("Mal posso esperar para ver seu próximo truque, " + mágico.title() + ".\n")
