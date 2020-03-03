"""
Às vezes, você vai querer escrever um prompt que seja maior que uma
linha. Por exemplo, talvez você queira explicar ao usuário por que está
pedindo determinada entrada. Você pode armazenar seu prompt em uma
variável e passá-la para a função input(). Isso permite criar seu prompt com
várias linhas e escrever uma instrução input() clara.
"""

prompt = "Se você nos disser quem é, podemos personalizar as mensagens."
prompt += "\nQual é o seu primeiro nome? "

nome = input(prompt)
print("\nOlá, " + nome)