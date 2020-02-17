nome = "ada lovelace"
print(nome.title()) #title() exibe cada palavra com uma letra maiúscula no início

print("----" * 4)

nome1 = "Ada Lovelace"
print(nome1.upper()) #upper() exibe cada palavra com uma letra maiúscula
print(nome1.lower()) #lower() exibe cada palavra com uma letra minúscula

print("----" * 4)

primeiro_nome = "ada"
ultimo_nome = "lovelace"
nome_completo = primeiro_nome + " " + ultimo_nome #concatenação de strings
mensagem = "Olá, " + nome_completo.title() + "!" #concatenação + formatação de strings

print(nome_completo)
print("Olá, " + nome_completo.title() + "!")
print(mensagem)

print("----" * 4)

print("\tPython") #O caractere \t serve como uma tabulação
print("Linguagens:\nPython\nC\nJavaScript") #O caractere \n serve como uma quebra de linha
print("Linguagens\n\tPython\n\tC\n\tJavaScript")

print("----" * 4)

linguagem_favorita = "python "
linguagem_favorita1 = " python "
print(linguagem_favorita.rstrip()) #rstrip() remove os espaços em branco no lado direito da string
print(linguagem_favorita1.lstrip()) #lstrip() remove os espaços em branco no lado esquerdo da string
print(linguagem_favorita1.strip()) #strip() remove os espaços em branco nos dois lados da string


