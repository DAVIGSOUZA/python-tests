print('oi')

# variables definition
# variables_name_convention

nomeDaVariavel = 'valor da variável'

print(nomeDaVariavel)

# define multiple variables

variavelA,variavelB = 'valor de A','valor de B'

print(variavelA,variavelB)

# type number, type boolean -> boleanos declarados sempre com inicial maiúscula
numero = 2
boleano = True
decimal = 2.2 #float

# returna o tipo da variável
print(type(nomeDaVariavel))
print(type(numero))
print(type(boleano))
print(type(decimal))


# strings
term = 'String de Exemplo'

# to lower case
print(term.lower())

# to upper case
print(term.upper())

# concat
print(term + " " + nomeDaVariavel)
# python não concatena tipos diferentes de dados, é preciso separar por virgula ou converter as variáveis
print(term + " " + str(boleano))
print(term, boleano)

# length
print(len(term))

# acessar posições dentro de uma string
ex = 'olá, fim'
print(ex[0])
print(ex[-1])

print(ex.index('f'))
print(ex.index('o'))

print(ex.replace('fim', 'python'))


# create function
def soma(a, b):
    print('você somou ', str(a), " e ", str(b), ": ", a + b)


soma(1,1)
soma(4,6)
soma(b=3, a=7)


def test_add(c,d): return c + d


print(test_add(2,6))


# multiple returns
def add_sub(e,f): return e + f, e - f


add, sub = add_sub(100, 50)


print(add)
print(sub)


#deletar variavel, o print causa erro no console pois a variavel não existe mais
del nomeDaVariavel
print(nomeDaVariavel)
