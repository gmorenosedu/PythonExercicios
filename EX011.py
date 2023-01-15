largura = float(input('Largura da parere: '))
altura = float(input('Altura da parere: '))
area = largura * altura
tinta = area / 2.0
print('Sua parede tem a dimensao de {} x {} e sua area e de {:.3f}m²  '.format(largura, altura, area))
print('Para pintar essa parede, voce precisara de {:.4f}l de tinta'.format(tinta))

