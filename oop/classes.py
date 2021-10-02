# ClassNameConvention

class Test:
  x = 25

print(Test)
# quando a classe não é instanciada python cria um objeto de mesmo nome
print(Test.x)

# instanciando um objeto
a = Test()

print(a.x)


class calc:
  def sum(self):
    return 2 + 8
  def example(self):
    print('This is a method')

b = calc()
print(b.sum())
b.example()

#constructor
#quando o objeto é iniciado executa o construtor -> __init__ 
class Construtor:
  def __init__(self):
      print('Obj criado com sucesso')

c = Construtor()

class ConstrutorArgs:
  def __init__(self, arg):
      print(arg)

d = ConstrutorArgs('obj criado com argumento')
