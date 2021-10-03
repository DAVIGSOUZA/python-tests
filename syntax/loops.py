# for
# função range nativa do python
for x in range(1,6):
  print('loop ' + str(x))

for i in 'this':
  print(i)

names = ['fulano', 'ciclano', 'outrano', 'thanos']

for name in names:
  print(name)

for x in range(6, 13):
  if x%2 == 0:
    print(x)

print('end of for')


# break | continue
for x in 'some string':
  if x == 'e':
    continue
  if x == 'i':
    break
  print(x)


for i in range(1, 3):
  print('loop1')
  for j in range(1, 4):
    print('loop2')

# while
count = 0
while count < 5:
  print(count)
  count += 1

print('end of while')


# fibonacci  \o/
a = 1
b = 1
while b <= 55:
  c = (a + b)
  print(c)
  a = b
  b = c


# loop se repete enquanto houver erro. 1 = error | 0 = no error
while(1):
  try:
    a = int(input('primeiro valor: '))
    b = int(input('segundo valor: '))
    print('resultado: ', a + b)
  except ValueError:
    print('informe numeros inteiros')
  except:
    print('erro desconhecido')
  else:
    print('alguma coisa depois de tudo')
  
  finally:
    print('valew falow')
