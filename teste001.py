n = input('Escreva algo:')
print ('Qual é o tipo primitivo do valor?' , type(n))
print("O valor é um alphanumerico?", n.isalnum())
print('O valor é um alfabeto?', n.isalpha())
print('O valor está maiúsculo?', n.isupper())
print('O valor está minúsculo?', n.islower())
print('O valor é um número?', n.isnumeric())
print('O valor só tem espaço?', n.isspace())
print('O valor está capitalizado?', n.istitle())