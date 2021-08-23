p= float(input('QUal o valor do produto? R$'))
d = (p*5)/100
print('Você obteve desconto de 5%, ou seja, {:.2f} reais'.format(d))
t = p-d
print('O valor do produto com desconto é {:.2f}'.format(t))