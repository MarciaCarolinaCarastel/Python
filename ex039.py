from datetime import date
print('\033[35mDescubra quanto tempo falta para se alistar no exército.')
nome = str(input('Me informe o sue nome:')).strip() .split()
ano = int(input('Qual o seu ano de nascimento?'))
c = date.today().year - ano
if c < 18:
    print('\033[33m',nome[0], ', você vai se alistar ao serviço militar em {} anos.'.format(18 - c))
elif c == 18:
    print('\033[32m', nome[0],', você precisa se alistar ao serviço militar este ano. Boa sorte.')
else:
    print('\033[31m',nome[0],', infelizmente já passou o seu período de alistamento há {} anos.'.format(c - 18))



