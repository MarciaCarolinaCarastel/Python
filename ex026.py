frase = str(input('Digite uma frase:')).strip()
frase = frase.upper()
print('A letra A aparece {} vezes em sua frase.'.format(frase.count('A')))
print('A letra A aparece pela primeira vez na posição {}'.format(frase.find('A') + 1)) # +1 para aparecer na tela a posição 1, que é mais lógica para nós
print('A letra A aparece pela última vez na posição {}.'.format(frase.rfind('A')+1)) # rfind para começar a contar de right (direita)

