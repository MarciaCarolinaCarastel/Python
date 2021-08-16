import math
n = float(input('Escreva um número real:'))
#b = math.floor(n)
#c = math.ceil(n)
#print('Você digitou {}.Seu valor arredondado para baixo é {}, e arredondado para cima é {}'.format(n,b,c))
print('Você digitou {}, e o seu valor inteiro é {}.'.format(n,math.trunc(n)))