a = int(input('Escreva o primeiro número:'))
b = int(input('Escreva o segundo valor:'))
c = int(input('Escreva o terceiro valor:'))
# O menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
# O maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O menor valor foi {}.'.format(menor))
print('O maior valor foi {}.'.format(maior))
