"""
Se você acidentalmente indentar um código que deva executar após um
laço ter sido concluído, esse código será repetido uma vez para cada
item da lista. Às vezes, isso faz Python informar um erro, mas,
geralmente, você terá um erro de lógica simples.
"""

mágicos = ['alice', 'david', 'carolina']
for mágico in mágicos:
    print(mágico.title() + ", isso foi um bom truque!")
    print("Mal posso esperar para ver seu próximo truque, " + mágico.title() + ".\n")

    print("Obrigado a todos. Esse foi um ótimo show de mágica!")