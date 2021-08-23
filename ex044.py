total = float(input('Bem vinda(o) à minha loja virtual. \nQual foi o valor total de suas compras?'))
print('Aqui estão suas opções de pagamento: \n1 - à vista dinheiro/cheque.\n2 - à vista no cartão. \n3 - 2x no cartão. \n4 - 3x ou mais no cartão. ')
método = int(input('Como deseja pagar?'))
if método == 1:
    print('Você recebeu 10% de desconto e pagará R${:.2f} à vista.'.format(total - (10 / 100 * total)))
elif método == 2:
    print('Você ganhou 5% de desconto, e pagará R${:.2f} no cartão.'.format(total - (5 / 100 * total)))
elif método == 3:
    print('Você pagará 2 parcelas de R${:.2f}'.format(total / 2))
elif método == 4:
    parcelas = int(input('Deseja parcelar em quantas vezes?'))
    print('Nesta modalidade existe um acréscimo de 20% de juros. Então você pagará {} parcelas de R${:.2f}'.format(parcelas, ((20 / 100 * total) + total) / parcelas))
else:
    print('OPÇÃO INVÁLIDA. ESCOLHA ENTRE 1 E 4.')

