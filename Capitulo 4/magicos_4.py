"""
Qualquer linha de código após o laço for que não estiver indentada será
executada uma vez, sem repetição. Vamos escrever um agradecimento ao
grupo de mágicos como um todo, agradecendo-lhes por apresentar um
show excelente. Para exibir essa mensagem ao grupo após todas as
mensagens individuais terem sido apresentadas, colocamos a mensagem de
agradecimento depois do laço for, sem indentação
"""

mágicos = ['alice', 'david', 'carolina']
for mágico in mágicos:
    print(mágico.title() + ", isso foi um bom truque!")
    print("Mal posso esperar para ver seu próximo truque, " + mágico.title() + ".\n")

print("Obrigado a todos. Esse foi um ótimo show de mágica!")