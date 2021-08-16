from math import hypot
co = float(input('Qual o valor do cateto oposto?'))
ca = float(input('Qual o valor do cateto adjacente?'))
h = hypot(co,ca)
print('O valor da hipotenusa do triângulo é: {:.2f}'.format(h))