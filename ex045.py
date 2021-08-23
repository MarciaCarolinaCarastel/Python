from random import choice
from time import sleep
print('=' * 20)
print('     JOKENPÔ')
print('=' * 20)
jogador = str(input('PEDRA, PAPEL OU TESOURA?')).strip().upper()
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
lista = ['PEDRA', 'PAPEL', 'TESOURA']
máquina = choice(lista)
if máquina == 'PEDRA':
    if jogador == 'PEDRA':
        print('EMPATE')
    elif jogador == 'PAPEL':
        print('VOCÊ VENCEU')
    elif jogador == 'TESOURA':
        print('VOCÊ PERDEU')
elif máquina == 'PAPEL':
    if jogador == 'PEDRA':
        print('VOCÊ PERDEU.')
    elif jogador == 'PAPEL':
        print('EMPATE.')
    elif jogador == 'TESOURA':
        print('VOCÊ VENCEU.')
elif máquina == 'TESOURA':
    if jogador == 'PEDRA':
        print('VOCÊ VENCEU')
    elif jogador == 'PAPEL':
        print('VOCE PERDEU')
    elif jogador == 'TESOURA':
        print('EMPATE')
else:
    print('OPÇÃO INVÁLIDA')


