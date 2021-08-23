print('10 TERMOS DE UMA PA')
termo = int(input('Me diga o primeiro termo:'))
razão = int(input('Me diga a rrazão de uma progressão aritmética:'))
décimo = termo + (10 - 1) * razão
for c in range(termo, décimo + razão, razão):
    print('{}'. format(c), end='-->')
