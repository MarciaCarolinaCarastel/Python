from time import sleep
print('CONTAGEM REGRESSIVA PARA VIRADA DO ANO')
for c in range(10, -1, -1):
    sleep(1)
    print(c)
print('\033[32mFELIZ ANO NOVO.')