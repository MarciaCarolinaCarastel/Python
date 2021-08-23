salario = float(input('Qual o valor do seu salário? R$'))
if salario > 1250:
    print('Você recebeu um aumento, e seu novo salário é R${:.2f}.'.format((salario * 10 / 100) + salario))
else:
    print('Você recebeu um aumento, e seu novo salário é R${:.2f}'.format((salario * 15/100) + salario))