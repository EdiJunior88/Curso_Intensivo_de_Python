"""
Escreva um laço que peça ao usuário para fornecer uma série de ingredientes
para uma pizza até que o valor 'quit' seja fornecido. À medida que cada
ingrediente é especificado, apresente uma mensagem informando que você
acrescentará esse ingrediente à pizza.
"""

print("Preparando uma pizza")
print("***************************************")
print("Digite quit para finalizar o programa")
print("***************************************")
print("Digite abaixo os ingredientes: ")

while True:
    mensagem = input("\n- ")
    if mensagem == 'quit':
        print("programa finalizado!".upper())
        break
    print("Adicionando " + mensagem + " na pizza")