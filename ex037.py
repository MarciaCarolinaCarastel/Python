numero = int(input('Me diga um número:'))
print('''Escolha uma das bases para conversão:
[1] BINÁRIO
[2] OCTAL
[3] HEXADECIMAL''')
opção = int(input('Sua opção:'))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(numero, bin(numero)[2:])) #utilizamos fatiamento para ignorar os primeiros dois digitos
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(numero, oct(numero)[2:])) #utilizamos fatiamento para ignorar os primeiros dois digitos
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(numero, hex(numero)[2:])) #utilizamos fatiamento para ignorar os primeiros dois digitos
else:
    print('Você não escolheu uma opção válida. Escolha entre 1 e 3.')

