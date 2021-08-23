import random
n1 = str(input('Aluno número 1:'))
n2 = str(input('Aluno número 2:'))
n3 = str(input('Aluno número 3:'))
lista = [n1,n2,n3]
sorteado = random.choice(lista)
print('O aluno sorteado foi {}'.format(sorteado))