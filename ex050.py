soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {}º número:'.format(c)))
    if num % 2 == 0:
        cont = cont + 1
        soma = soma + num
print('Temos {} valores pares e a soma deles é {}.'.format(cont, soma))
