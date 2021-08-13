import math
ang = int(input('Digite o angulô que deseja:'))
cos = math.cos(math.radians(ang))
sen = math.sin(math.radians(ang))
tang = math.tan(math.radians(ang))
print('O seno de {} é {:.2f}, o cosseno é {:.2f}, e a tangente é {:.2f}.'.format(ang,sen,cos,tang))