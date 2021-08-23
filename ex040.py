print('Vamos calcular sua média?')
n1 = float(input('Digite a sua nota do primeiro bimestre:'))
n2 = float(input('Digitei a sua nota do segundo bimestre:'))
média = (n1 + n2) / 2
if média < 5.0:
    print('\033[31mInfelizmente você foi reprovado.')
elif média > 7.0:
    print('\033[32mParabéns, você foi aprovado.')
elif 7 > média >= 5:
    print('\033[33mVocê está em recuperação. Espero que obtenha sucesso.')