"""
Escreva versões diferentes do Exercício 7.4 ou do Exercício 7.5
que faça o seguinte, pelo menos uma vez:

• use um teste condicional na instrução while para encerrar o laço;

• use uma variável active para controlar o tempo que o laço executará;

• use uma instrução break para sair do laço quando o usuário fornecer o valor 'quit'
"""
print("Preço do Ingresso do Parque de Diversões")
print("*****************************************")
print("Digite quit para finalizar o programa:")
print("*****************************************")

active = True

while True:
    idade = input("\nDigite a sua idade: ")
    if idade == 'quit':
        print("PROGRAMA FINALIZADO")
        break

    if int(idade) < 3:
        print("Ingresso gratuito.")
    elif int(idade) <= 12:
        print("Preço do Ingresso: R$ 10,00")
    else:
        print("Preço do Ingresso: R$ 15,00")