"""
Use um dicionário para armazenar os números favoritos
de algumas pessoas. Pense em cinco nomes e use-os como chaves em seu
dicionário.

Pense em um número favorito para cada pessoa e armazene cada um
como um valor em seu dicionário. Exiba o nome de cada pessoa e seu número
favorito. Para que seja mais divertido ainda, faça uma enquete com alguns amigos
e obtenha alguns dados reais para o seu programa
"""

numeros_favoritos = {
    'nome': 'cléber', 'número': 50,
    'nome1': 'junior', 'número1': 26,
    'nome2': 'amanda', 'número2': 1,
    'nome3': 'cássia', 'número3': 13,
    'nome4': 'érica', 'número4': 20,
}

print("Nome:", numeros_favoritos['nome'].title(), "- Número Favorito:", numeros_favoritos['número'])
print("Nome:", numeros_favoritos['nome1'].title(), "- Número Favorito:", numeros_favoritos['número1'])
print("Nome:", numeros_favoritos['nome2'].title(), "- Número Favorito:", numeros_favoritos['número2'])
print("Nome:", numeros_favoritos['nome3'].title(), "- Número Favorito:", numeros_favoritos['número3'])
print("Nome:", numeros_favoritos['nome4'].title(), "- Número Favorito:", numeros_favoritos['número4'])