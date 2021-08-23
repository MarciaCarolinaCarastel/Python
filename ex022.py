nome = str(input('Qual é o seu nome completo?')).strip()
print ('Seu nome em maiúsculo é:',nome.upper())
print ('Seu nome em minúsculo é:', nome.lower())
print ('Seu nome todo tem {} letras'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
lista = nome.split()
print ('Seu primeiro nome tem {} letras'.format(len(lista[0])))




