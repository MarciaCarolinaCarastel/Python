import random
from time import sleep     ## importar modo 'soneca' do sistema
sorteio = random.randint(0,5)
print('\033[1;35mEstou pensando em um número de 0 a 5.')
a = int(input('Você consegue adivinhar?'))
print('\033[33mPROCESSANDO...')
sleep(2)    #soneca por 2 segundos
if a == sorteio:
    print('\033[1;32mEu pensei no número {}. Parabéns, você acertou!'.format(sorteio))
else:
    print('\033[1;31mFooon, você errou. \nEu pensei no número {}, e não no número {}.'.format(sorteio,a))