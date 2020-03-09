"""
Considere uma lista de usuários recém-registrados em um site, porém não
verificados. Depois de conferir esses usuários, como podemos transferi-los
para uma lista separada de usuários confirmados? Uma maneira seria usar
um laço while para extrair os usuários da lista de usuários não confirmados
à medida que os verificarmos e então adicioná-los em uma lista separada
de usuários confirmados. Esse código pode ter o seguinte aspecto:
"""

#Começa com os usuários que precisam ser verificados,
# e com uma lista vazia para armazenar os usuários confirmados

usuarios_nao_confirmados = ['alice', 'brian', 'candace']
usuarios_confirmados = []

#verifica cada usuario ate que não haja mais usuários não confirmados
#Transfere cada usuário verificado para a lista de usuários confirmados

while usuarios_nao_confirmados:
    usuario_atual = usuarios_nao_confirmados.pop()

    print("Verificando usuário: " + usuario_atual.title())
    usuarios_confirmados.append(usuario_atual)

#Exibe todos os usuários confirmados
print("\nOs seguintes usuários foram confirmados:")
for usuario_confirmado in usuarios_confirmados:
    print(usuario_confirmado.title())