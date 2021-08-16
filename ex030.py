numero = int(input('Me diga um número:'))
unidade = (numero // 1 % 10) % 2 #Se o resto da divisão da unidade for igual a 0, então ele é par
if unidade == 0:
    print('Seu número é par.')
else:
    print('Seu número é impar.')