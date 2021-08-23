from datetime import date
print('Vamos ver em que categoria você vai competir?')
ano = int(input('Qual o ano do seu nascimento?'))
idade = date.today().year - ano
if idade <= 9:
    print('Você é da categoria MIRIM.')
elif idade <= 14:
    print('Você é da categoria INFANTIL.')
elif idade <= 19:
    print('Você é da Categoria JUNIOR.')
elif idade <= 25:
    print('Você é da categoria SÊNIOR.')
else:
    print('Você é da categoria MASTER.')
