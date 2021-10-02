
# dicionary, semelhante a obj do JS
numberKeys = {
  1: 'valor',
  2: 'outro valor'
}
print(numberKeys)

obj = {
  'chave': 'valor',
  'igual': 'a um JSON'
}

print(obj)

# acessando valores
print(obj.get('chave'))
print(obj['chave'])

# mudando valor
obj['chave'] = 'novo valor'
print(obj)

# limpando dic
obj.clear()
print(obj)

newObj = {
  'chave': 'valor',
  'outra chave': 'deletar',
  'string': 'terceiro valor',
  'numero': 1,
  'boolean': True,
  'float': 1.223423
}

# length
print(len(newObj))

# deletando chave-valor
del newObj['outra chave']
print(newObj)