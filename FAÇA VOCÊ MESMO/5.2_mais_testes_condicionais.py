"""
Você não precisa limitar o número de testes que criar em dez. Se quiser testar mais comparações,
escreva outros testes e acrescenteos em conditional_tests.py. Tenha pelo menos um resultado True
e um False paracada um dos casos a seguir:

• testes de igualdade e de não igualdade com strings;
• testes usando a função lower();
• testes numéricos que envolvam igualdade e não igualdade, maior e menor que,
maior ou igual a e menor ou igual a;
• testes usando as palavras reservadas and e or;
• testes para verificar se um item está em uma lista;
• testes para verificar se um item não está em uma lista
"""
print("Escolha entre os climas: Ensolarado / Chuvoso / Nublado:")
clima = "Chuvoso"
print("---------------------------------------------------------")
print("Resposta selecionada:", clima)
print("---------------------------------------------------------")

if clima == "Nublado":
    print("Não poderei sair agora porque o tempo está", clima)
elif clima == "Ensolarado" or clima == "Nublado":
    print("Agora posso sair porque o tempo está", clima)
elif clima == "Chuvoso":
    print("Não posso sair, a rua está inundada porque o tempo está", clima)
else:
    print("Resposta Inválida! Tente Novamente!")