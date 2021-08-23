print('Calcule seu IMC')
peso = float(input('Digite o seu peso(KG):'))
altura = float(input('Digite a sua altura(m):'))
imc = peso / (altura ** 2)
print('Seu imc é de {:.1f}'.format(imc))
if imc <= 18.5:
   print('Você está ABAIXO do peso.')
elif imc < 25:
   print('Seu peso está IDEAL.')
elif imc < 30:
   print('Você está com SOBREPESO.')
elif imc < 40:
   print('Você está com OBESIDADE.')
else:
   print('OBESIDADE MÓRBIDA.')