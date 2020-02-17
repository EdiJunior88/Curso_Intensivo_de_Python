bicicletas = ['trek', 'cannondale', 'redline', 'specialized']
print(bicicletas)
print(bicicletas[0]) #acessando um elemento de uma lista
print(bicicletas[0].title()) #podemos formatar o elemento 'trek' de modo mais bonito usando o método title()
print(bicicletas[1]) #cannondale
print(bicicletas[3]) #specialized
print(bicicletas[-1]) #Ao solicitar o item no índice -1, Python sempre devolve o último item da lista (specialized)

mensagem = "Minha primeira bicicleta foi a " + bicicletas[0].title() + "."
print(mensagem)