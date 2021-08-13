numero = int(input('Digite um número de 0 a 9999:'))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('A unidade do número digitado é {}'.format(u))
print('A dezena do número digitado é {}'.format(d))
print('A cenena do número digitado é {}'.format(c))
print ('O milhar do número digitado é {}'.format(m))

