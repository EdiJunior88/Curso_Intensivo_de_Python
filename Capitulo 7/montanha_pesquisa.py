"""
Podemos pedir a quantidade de entrada que for necessária a cada passagem
por um laço while. Vamos criar um programa de enquete em que cada
passagem pelo laço solicita o nome do participante e uma resposta.
Armazenaremos os dados coletados em um dicionário, pois queremos
associar cada resposta a um usuário em particular:
"""

respostas = {}

#Define uma flag para indicar que a enquete está ativa
pesquisa_ativa = True

while pesquisa_ativa:
    #Pede o nome da pessoa e a resposta
    nome = input("\nQual é o seu nome? ")
    resposta = input("Qual montanha você gostaria de escalar um dia? ")

    #Armazena a resposta no dicionário
    respostas[nome] = resposta

    #Descobre se outra pessoa vai responder à enquete
    repetir = input("Gostaria de deixar outra pessoa responder? (Sim / Não) ")
    if repetir == 'não':
        pesquisa_ativa = False

#A enquete foi concluída. Mostra os resultados
print("\n--- Resultados da Pesquisa ---")
for nome, resposta in respostas.items():
    print(nome + " gostaria de subir no(a) " + resposta + ".")