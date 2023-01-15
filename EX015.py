dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
total = (dias * 60.0) + (km * 0.15)
print('O total a pagar e de R$ {:.2f}'.format(total))

