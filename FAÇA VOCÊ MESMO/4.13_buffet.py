"""
Um restaurante do tipo buffet oferece apenas cinco tipos básicos de
comida. Pense em cinco pratos simples e armazene-os em uma tupla.

• Use um laço for para exibir cada prato oferecido pelo restaurante.
• Tente modificar um dos itens e cerifique-se de que Python rejeita a mudança.
• O restaurante muda seu cardápio, substituindo dois dos itens com pratos
diferentes. Acrescente um bloco de código que reescreva a tupla e, em seguida,
use um laço for para exibir cada um dos itens do cardápio revisado
"""

comidas = ('carne moída', 'arroz', 'feijão', 'salsicha', 'ovos')

# comidas[0] = 'salada' #erro proposital, não se acrescenta um item na tupla desse modo

print("Comidas do Buffet:")
for comida in comidas:
    print("-", comida)

print("\nAcrescentando mais duas comidas no cardápio\n")

comidas = ('carne moída', 'arroz', 'feijão', 'bife', 'peixe')
print("Comidas do Buffet:")
for comida in comidas:
    print("-", comida)