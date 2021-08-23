print('Números impares, multiplos de 3, entre 1 e 500.')
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1 # contador conta mais um encontrado
        soma = soma + c # acumulador acumula os valores
print('A soma de todos os {} valores é {}.'.format(cont, soma))