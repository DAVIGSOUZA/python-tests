my_list = [11, 'olá', True]

print(my_list)
print(my_list[1])
print(my_list[-1])
print(my_list.index(11))
print(my_list.index('olá'))
print(my_list.index(True))

# primeiro arg é o inicio, segundo arg é o final excludente, ex: [1:8] inicío = index 1 | fim = index 7
print(my_list[0:2])

# sem o primeiro arg retorna tudo ANTES do indice do segundo argumento
print(my_list[:2])

# sem o segundo argumento returna tudo a PARTIR do primeiro argumento
print(my_list[2:])

# mudar valor de um elemento da lista
my_list[-1] = False

print(my_list)

# adicionar elemento a lista
my_list.append('novo elemento')

print(my_list)

# inserir novo elemento em um index especifico da lista
# primeiro arg é o index da lista, segundo argumento é o elemento a ser inserido naquele index
my_list.insert(1, 12)
print(my_list)

# remover elemento da lista
my_list.remove(12)
print(my_list)
my_list.remove(my_list[-1])
print(my_list)


#  limpar lista
my_list.clear()
print(my_list)


complexList = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

print(complexList[0][-1])


# define a tuple
# listas são mutaveis, tuples são imutáveis 
my_tuple = (11, 'olá', True)


