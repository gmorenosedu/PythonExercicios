from math import sin, cos, tan, radians
ang = float(input('Digite o angulo que você deseja: '))
seno = sin(radians(ang))
coseno = cos(radians(ang))
tangente = tan(radians(ang))

print('O angulo de {} tem o SENO de {:.2f}'.format(ang, seno))
print('O angulo de {} tem o COSSENO de {:.2f} '.format(ang, coseno))
print('O angulo de {} tem o TANGENTE de {:.2f} '.format(ang, tangente))

