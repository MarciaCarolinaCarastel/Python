r1 = float(input('\033[1;34mMe informe uma medida:'))
r2 = float(input('Me informe uma medida:'))
r3 = float(input('Me informe uma medida:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[32mEssas medidas formam um triângulo.',end='')
    if r1 == r2 == r3:
        print(' EQUILÁTERO.')
    elif r1 != r2 != r3 != r1:
            print('ESCALENO.')
    else:
        print('ISÓSCELES.')
else:
    print('\033[31mEssas medidas não formam um triângulo.')