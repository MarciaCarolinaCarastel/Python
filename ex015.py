d = int(input('Quantos dias alugados?'))
k = float(input('Quantos km você percorreu?'))
# dia = d * 60
# km = k * 0.15
# t = dia + km
t = (d * 60) + (k * 0.15)
print('Você pagará R${:.2f}.'.format(t))





