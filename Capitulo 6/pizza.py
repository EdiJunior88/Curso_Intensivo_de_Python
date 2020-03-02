"""
No exemplo a seguir, dois tipos de informação são armazenados para
cada pizza: o tipo de massa e a lista de ingredientes. A lista de ingredientes
é um valor associado à chave 'toppings'. Para usar os itens da lista,
fornecemos o nome do dicionário e a chave 'toppings', como faríamos com
qualquer valor do dicionário. Em vez de devolver um único valor, teremos
uma lista de ingredientes:
"""

#Armazena informações sobre uma pizza que está sendo pedida
pizza = {
    'casca': 'grossa',
    'coberturas': ['cogumelo', 'queijo extra'],
}

#Resume o pedido
print("Você pediu a pizza com a casca " + pizza['casca'] + " e com a seguinte cobertura:")

for cobertura in pizza['coberturas']:
    print("\t" + cobertura)