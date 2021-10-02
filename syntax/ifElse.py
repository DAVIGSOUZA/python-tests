a = 2
b = 2
c = 3
d = 3

if a == b:
  print('a é igual a b')

if a == c:
  print('não vai retornar true')
else:
  print('a não é igual a c')

if b == c:
  print('não vai retornar true')
elif c == d:
  print('c é igual a d')
else:
  print('não vai entrar no else')


if a == b and c == d:
  print('retornou true')

if a == c or c == d:
  print('retornou true')

if not a == c:
  print('a não é igual a c')


x = int(input('informe um numero entre 100 e 300: '))

if x < 150:
  print('valor é menor que 150')
  if x == 100:
    print('valor é igual a 100')
  elif x == 125:
    print('valor é igual a 125')
  else:
    print('valor não é 100 nem 125')
else:
  print('valor é maior que 150')