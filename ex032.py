from datetime import date
ano = int(input('Qual ano você quer analisar? Digite 0 caso queira analisar o ano atual.:'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:   ##divisivel por 4, exceto anos multiplos de 100 que não são multiplos de 400
    print('O ano de {} é bissexto!'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))