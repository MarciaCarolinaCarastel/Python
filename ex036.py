f = str(input('\033[33mVocê deseja financiar uma casa conosco?\033[m')).capitalize().strip() ## ainda não sei como criar if mais aninhado para perguntar se sim ou se nao finalizar
print('Beleza, precisamos de alguns dados seus.')
nome = str(input('Me informe seu nome completo:')).split()
salario = float(input('Agora preciso saber qual o seu salário: R$'))
casa = float(input('Qual o valor da casa que deseja financiar?'))
anos = int(input('Em quantos meses deseja pagar?'))
parcela = casa / anos
print(nome[0],', você pagará R${:.2f} por mês'.format(parcela))
porcentagem = (salario * 30) / 100
if parcela > porcentagem:
        print('\033[31mSeu salário é incompatível com o financiamento.')
elif parcela < porcentagem:
    print('\033[32mParabéns. Seu financiamento foi aprovado')



