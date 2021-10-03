# para tornar um método ou variável privado adiciona-se 2 underscore antes do nome: __exemplo
class Courses:
  # public variable
  student = 55
  # private variable
  __username = 'fulano'

  # public method
  def std_strength(self):
    print('this is a public method')
  
  # private method
  def __std_username(self):
    print('this is a private method')


class Test:
  a = Courses()

  # public
  a.std_strength()
  print(a.student)

  # # private: erro no console, pois a classe Test não possui acesso aos métodos privados de Courses
  # a.__std_username()
  # print(a.__username)

  # para acessar o método privado fazer como abaixo
  a._Courses__std_username()
  print(a._Courses__username)

class OtherTest(Courses):
  def __init__(self):
      print('other test constructor')

o = OtherTest()

# private access
print(o._Courses__username)
o._Courses__std_username()

# console error
print(o.__username)
o.__std_username()

