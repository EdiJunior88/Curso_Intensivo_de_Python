"""
Crie um dicionário chamado cities. Use os nomes de três
cidades como chaves em seu dicionário. Crie um dicionário com informações sobre
cada cidade e inclua o país em que a cidade está localizada, a população
aproximada e um fato sobre essa cidade. As chaves do dicionário de cada cidade
devem ser algo como country, population e fact. Apresente o nome de cada
cidade e todas as informações que você armazenou sobre ela.
"""

cidades = {

    'maceió': {
        'país': 'brasil',
        'população': 1.012382,
        'fato': 'belas praias',
    },

    'milão': {
        'país': 'itália',
        'população': 1.308735,
        'fato': 'captal da moda e design',
    },

    'tóquio': {
        'país': 'japão',
        'população': 13.5038102,
        'fato': 'centro político, financeiro, comercial e educacional',
    },
}

for cidade, informação in cidades.items():
    país = informação['país'].title()
    população = informação['população']
    fato = informação['fato']

    print("Cidade: " + cidade.title())
    print("País: " + país.title())
    print("População: " + str(população) + " de habitantes.")
    print("Fato Curioso: " + fato.capitalize() + "." + "\n")