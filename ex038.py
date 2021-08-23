print('\033[33mMe diga dois números, e eu te direi qual é o maior. Vamos começar?\033[m')
n1 = int(input('Me diga o primeiro número:'))
n2 = int(input('Me diga outro número:'))
if n1 > n2:
    print('O primeiro valor é maior.')
elif n2 > n1:
    print('O segundo valor é maior.')
else:
    print('Opa, não existe valor maior. Os dois são iguais.')