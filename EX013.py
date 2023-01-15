atual = float(input('Qual e o salario do Fuincionario? R$ '))
novo = atual + (atual * 15 / 100)
print('Um funcionario que ganhava R$ {:.2f}, com 15% de aumento, passa a receber R$ {:.2f}'.format(atual, novo))
