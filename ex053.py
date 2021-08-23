print('Palindromos são frases que podem ser lidas ao contrário. Vamos tentar?')
frase = str(input('Digite uma frase:')).strip().upper()
palavra = frase.split()
juntar = ''.join(palavra)
inverso = juntar[::-1]
print(juntar, inverso)
if inverso == frase:
    print('Temos um palíndromo.')
else:
    print('NÃO temos um palíndromo.')

