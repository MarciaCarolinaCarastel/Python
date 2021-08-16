r1 = float(input('\033[1;34mMe informe uma medida:'))
r2 = float(input('Me informe uma medida:'))
r3 = float(input('Me informe uma medida:'))
t = r1 + r2 and r2 < r1 + r3 and r3< r1+ r2
if t > r3:
    print('\033[32mEssas medidas formam um triângulo.')
else:
    print('\033[31mEssas medidas não formam um triângulo.')