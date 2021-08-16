velocidade = float(input('Qual a velocidade do seu carro?'))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print('Você excedeu a velocidade média, e vai ser multado em R${:.2f}.'.format(multa))
else:
    print('Ok. Você estava no limite da velocidade ')