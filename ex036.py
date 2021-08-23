f = str(input('\033[33mVocê deseja financiar uma casa conosco?\033[m')).strip().lower()
if f == 'sim':
    print('Beleza, precisamos de alguns dados seus.')
    nome = str(input('Me informe seu nome completo:')).split()
    salario = float(input('Agora preciso saber qual o seu salário: R$'))
    casa = float(input('Qual o valor da casa que deseja financiar?'))
    anos = int(input('Em quantos anos deseja pagar?'))
    parcela = casa / (anos * 12)
    print(nome[0],', você pagará R${:.2f} por mês'.format(parcela))
    porcentagem = (salario * 30) / 100
    if parcela > porcentagem:
        print('\033[31mSeu salário é incompatível com o financiamento. Empréstimo NEGADO.')
    elif parcela <= porcentagem:
        print('\033[32mParabéns. Seu financiamento foi aprovado. Empréstimo concedido.')
else:
    print('Ok. Tenha um bom dia.')



