# ClassNameConvention

class Test:
  x = 25

print(Test)
# quando a classe não é instanciada python cria um objeto de mesmo nome
print(Test.x)

# instanciando um objeto
a = Test()

print(a.x)

# definição de métodos da classe
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




# instancias
# palavra chave "self" remete a instancia daquele objeto
class ExemploInstancia:
    def __init__(self, name):
        print('Construtor do exemplo de instancia')
        print('Tudo inicializado dentro do construtor é preciso conter a palavra chave: "self"')
        self.name = name

    def instance_method(self):
      print('instance method')
      print('nome', self.name)

objeto = ExemploInstancia('Thanos')
outro_objeto = ExemploInstancia('Tiranos')
objeto.instance_method()
outro_objeto.instance_method()



# métodos estáticos
# não é preciso lidar com o construtor
# chamada direta do método passando os argumentos necessários
# opcionalmente é possivel passar o decorator @staticmethod antes da declaração
class ExemploStatic:
  def __init__(self):
    print('construtor do exemplo de método estatico')
  
  def static_method(str_arg):
    print('método estático', str_arg)

estatico = ExemploStatic.static_method('argumento estatico')
ExemploStatic.static_method('argumento do método estatico')




# método de classe
# para declarar métodos de classe:
# adicionar o decorator @classmethod
# passar como argumento do método "cls"
class ExemploClassMethod:
  def __init__(self):
    print('construtor do exemplo de método de classe')

  @classmethod
  def class_method(cls):
    print('chamou class method')
    cls.static_method('argumento estatico dentro do método de classe')

  @staticmethod
  def static_method(str_arg):
    print('método estático', str_arg)

metodo_classe = ExemploClassMethod()
metodo_classe.class_method()




# classe com argumento opcional
class Overload:
  def __init__(self):
    print('constructor')

  def soma_tres(a, b, c = 0):
    print(a + b + c)

  def run(self, name = None, age = None):
    if name == None:
      print('no arg')
    else:
      print('arg was inputed')


Overload.soma_tres(1,2, 10)
  

o = Overload()
o.run()
o.run('blablabla')


# exemplo de overloading
class Circle:
  def __init__(self, radius):
    self.radius = radius
  
  def set_radius(self,radius):
    self.radius = radius

  def get_radius(self):
    return self.radius

  def area(self):
    return 3.14 * self.radius ** 2

  def __add__(self, another_circle):
    return Circle(self.radius + another_circle.radius)
  

c1 = Circle(5)
print(c1.get_radius())

c2 = Circle(6)
print(c2.get_radius())

c3 = c1 + c2

print(c3.get_radius())