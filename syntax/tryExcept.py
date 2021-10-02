try:
  age = int(input('Informe sua idade: '))
  if age <= 18:
    print('vc é noob')
except:
  print('informe um número')
else:
  print('você tem ', age, ' anos')


# tratando erros
try:
  a = int(input('primeiro valor: '))
  b = int(input('segundo valor: '))
  print('resultado: ', a + b)
except ValueError:
  print('informe numeros inteiros')
except:
  print('erro desconhecido')

finally:
  print('valew falow')


# criando execessão
x = int(input('informe numero positivo: '))
if x < 0:
  raise Exception('esperado valor positivo.')
else:
  print(x)

try:
  y = int(input('informe numero positivo: '))
  if y < 0 :
    raise ValueError
except ValueError:
  print('ERRO: informe numero positivo')